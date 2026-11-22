
import streamlit as st
import tensorflow as tf
import numpy as np
import json
from pathlib import Path
from PIL import Image
from io import BytesIO
from disease_info import get_disease_info
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as PDFImage
from xml.sax.saxutils import escape

# Project folder paths
BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "assets" / "CropDoc_AI_Logo.png"
MODEL_PATH = BASE_DIR / "models" / "cropdoc_model.h5"
CLASS_PATH = BASE_DIR / "models" / "class_names.json"

# Page configuration
st.set_page_config(
    page_title="CropDoc AI",
    page_icon="🌱",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
<style>
    .main {
        background-color: #f5f9f4;
    }

    .main-title {
        text-align: center;
        color: #216b3a;
        font-size: 42px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #52665a;
        font-size: 17px;
        margin-bottom: 25px;
    }

    .section-title {
        color: #216b3a;
        font-size: 23px;
        font-weight: bold;
    }

    .result-card {
        background-color: #e8f5e9;
        color: #1b4332;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #2e8b57;
        margin-bottom: 15px;
    }

    .result-card h3,
    .result-card h4 {
        color: #1b4332 !important;
    }

    .info-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #dce9dd;
        margin-bottom: 15px;
    }

    .footer {
        text-align: center;
        color: #718078;
        font-size: 13px;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)


# Load model only once
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


model = load_model()

# Load disease categories
with open(CLASS_PATH, "r") as file:
    class_names = json.load(file)

# Sidebar information
with st.sidebar:
    st.title("🌱 CropDoc AI")

    st.write("### About the Project")

    st.write(
        "CropDoc AI is a deep learning-based application "
        "that identifies plant leaf disease categories "
        "from uploaded images."
    )

    st.divider()

    st.write("### Project Details")

    st.write("**Domain:** Agriculture and AI")

    st.write("**Model:** MobileNetV2")

    st.write("**Framework:** TensorFlow / Keras")

    st.write("**Interface:** Streamlit")

    st.write("**Dataset:** PlantVillage")

    st.write("**Categories:** 38")

    st.divider()

    st.write("### Supported Crops")

    st.write(
        "Apple, Blueberry, Cherry, Corn, Grape, Orange, "
        "Peach, Bell Pepper, Potato, Raspberry, Soybean, "
        "Squash, Strawberry and Tomato."
    )

    st.divider()

    st.caption(
        "Educational project. AI predictions are not "
        "confirmed plant disease diagnoses."
    )

# Application header
st.markdown(
    '<div class="main-title">🌱 CropDoc AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Intelligent Plant Disease Detection and Classification '
    'Using Deep Learning'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

st.markdown(
    "### 🌿 Welcome to CropDoc AI"
)

st.write(
    "Upload a clear photograph of a plant leaf. "
    "Our deep learning model will analyse the image "
    "and predict its plant health category."
)


# Image upload section
st.markdown(
    '<div class="section-title">📸 Upload Plant Image</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)


# Process uploaded image
if uploaded_file is not None:

    image = Image.open(
        BytesIO(uploaded_file.getvalue())
    ).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            image,
            caption="Uploaded Plant Leaf",
            width=350
        )

    with col2:
        st.markdown("### Image Details")
        st.write("**File name:**", uploaded_file.name)
        st.write("**Image format:**", image.format or "RGB")
        st.write("**Image dimensions:**", image.size)

        st.write(
            "Make sure the leaf is clearly visible "
            "for better image analysis."
        )

    st.divider()

    # Prediction button
    if st.button(
        "🔍 Predict Plant Disease",
        use_container_width=True
    ):

        with st.spinner("Analysing plant image..."):

            # Resize image
            resized_image = image.resize((160, 160))

            # Convert image to NumPy array
            image_array = np.array(resized_image)

            # Add batch dimension
            image_array = np.expand_dims(
                image_array,
                axis=0
            )

            # Make prediction
            predictions = model.predict(
                image_array,
                verbose=0
            )

            # Get predicted category
            predicted_index = np.argmax(predictions[0])
            predicted_class = class_names[predicted_index]

            # Calculate confidence
            confidence = float(
                predictions[0][predicted_index] * 100
            )

            # Format category name
            display_name = (
                predicted_class
                .replace("___", " - ")
                .replace("_", " ")
            )

            # Get disease information
            disease_info = get_disease_info(
                predicted_class
            )

        # Prediction result
        st.divider()
        st.markdown(
            '<div class="section-title">📊 Prediction Results</div>',
            unsafe_allow_html=True
        )

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.markdown(
                '<div class="result-card">'
                '<h4>Predicted Category</h4>'
                '<h3>' + display_name + '</h3>'
                '</div>',
                unsafe_allow_html=True
            )

        with result_col2:
            st.markdown(
                '<div class="result-card">'
                '<h4>Confidence Score</h4>'
                '<h3>' + str(round(confidence, 2)) + '%</h3>'
                '</div>',
                unsafe_allow_html=True
            )

        st.write("**Model confidence visualization**")

        st.progress(
            min(max(confidence / 100, 0.0), 1.0)
        )

        st.info(
            "This is an AI-generated prediction. "
            "It is not a confirmed plant disease diagnosis."
        )

        # Plant health information
        st.divider()

        st.markdown(
            '<div class="section-title">🌱 Plant Health Information</div>',
            unsafe_allow_html=True
        )

        st.success(disease_info["status"])

        st.markdown("### Disease Information")
        st.write(disease_info["description"])

        # Symptoms and tips
        symptom_col, tips_col = st.columns(2)

        with symptom_col:
            st.markdown("### 🔎 Common Symptoms")

            for symptom in disease_info["symptoms"]:
                st.markdown("- " + symptom)

        with tips_col:
            st.markdown("### 🌿 Prevention and Care Tips")

            for tip in disease_info["tips"]:
                st.markdown("- " + tip)
        
       
        # Generate downloadable PDF report
        pdf_buffer = BytesIO()

        # Create PDF document
        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=A4,
            rightMargin=50,
            leftMargin=50,
            topMargin=50,
            bottomMargin=50
        )

        # Define PDF styles
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "ReportTitle",
            parent=styles["Title"],
            textColor=colors.HexColor("#216b3a"),
            alignment=TA_CENTER,
            fontSize=22,
            spaceAfter=20
        )

        heading_style = ParagraphStyle(
            "SectionHeading",
            parent=styles["Heading2"],
            textColor=colors.HexColor("#216b3a"),
            spaceBefore=12,
            spaceAfter=8
        )

        body_style = styles["BodyText"]

        # Add content to PDF
        story = []
        # Add CropDoc AI logo
        if LOGO_PATH.exists():
            logo = PDFImage(str(LOGO_PATH))
            max_logo_width = 160
            max_logo_height = 75

            scale = min(
                max_logo_width / logo.imageWidth,
                max_logo_height / logo.imageHeight
            )

            logo.drawWidth = logo.imageWidth * scale
            logo.drawHeight = logo.imageHeight * scale
            logo.hAlign = "CENTER"

            story.append(logo)
            story.append(Spacer(1, 10))

        story.append(
            Paragraph("CROPDOC AI", title_style)
        )

        story.append(
            Paragraph(
                "Plant Disease Detection Report",
                styles["Heading2"]
            )
        )

        story.append(Spacer(1, 10))

        # Add uploaded leaf photograph
        leaf_buffer = BytesIO()
        image.save(leaf_buffer, format="PNG")
        leaf_buffer.seek(0)

        leaf_pdf = PDFImage(leaf_buffer)

        # Maintain original image proportions
        max_width = 220
        max_height = 180

        scale = min(
            max_width / leaf_pdf.imageWidth,
            max_height / leaf_pdf.imageHeight
        )

        leaf_pdf.drawWidth = leaf_pdf.imageWidth * scale
        leaf_pdf.drawHeight = leaf_pdf.imageHeight * scale
        leaf_pdf.hAlign = "CENTER"

        story.append(leaf_pdf)
        story.append(Spacer(1, 15))

        story.append(
            Paragraph(
                "<b>Date and Time:</b> "
                + escape(datetime.now().strftime("%d-%m-%Y %H:%M:%S")),
                body_style
            )
        )

        story.append(Spacer(1, 12))

        story.append(
            Paragraph("Prediction Results", heading_style)
        )

        story.append(
            Paragraph(
                "<b>Predicted Category:</b> "
                + escape(display_name),
                body_style
            )
        )

        story.append(
            Paragraph(
                "<b>Confidence Score:</b> "
                + str(round(confidence, 2)) + "%",
                body_style
            )
        )

        story.append(
            Paragraph(
                "<b>Plant Health Status:</b> "
                + escape(disease_info["status"]),
                body_style
            )
        )

        story.append(
            Paragraph("Disease Information", heading_style)
        )

        story.append(
            Paragraph(
                escape(disease_info["description"]),
                body_style
            )
        )

        story.append(
            Paragraph("Common Symptoms", heading_style)
        )

        for symptom in disease_info["symptoms"]:
            story.append(
                Paragraph("- " + escape(symptom), body_style)
            )

        story.append(
            Paragraph("Prevention and Care Tips", heading_style)
        )

        for tip in disease_info["tips"]:
            story.append(
                Paragraph("- " + escape(tip), body_style)
            )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                "<b>Disclaimer:</b> This is an AI-generated prediction. "
                "It is not a confirmed plant disease diagnosis.",
                body_style
            )
        )

        # Generate PDF
        doc.build(story)

        pdf_data = pdf_buffer.getvalue()

        # Download button
        st.divider()
        st.subheader("📄 Download PDF Prediction Report")

        st.download_button(
            label="⬇️ Download PDF Report",
            data=pdf_data,
            file_name="CropDoc_AI_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )


# Footer
st.divider()

st.markdown(
    '<div class="footer">'
    '🌱 CropDoc AI | Deep Learning Based Plant Disease Detection'
    '<br>Educational project – AI predictions should be verified '
    'through appropriate plant inspection.'
    '</div>',
    unsafe_allow_html=True
)
