
def get_disease_info(disease_name):

    disease_data = {

        # APPLE DISEASES
        "Apple___Apple_scab": {
            "status": "Possible Apple Scab",
            "description": "Apple scab is a fungal disease affecting apple leaves and fruits.",
            "symptoms": [
                "Olive-green or dark spots on leaves.",
                "Velvety lesions on leaf surfaces.",
                "Dark, rough spots on fruits.",
                "Leaf distortion in severe cases."
            ],
            "tips": [
                "Collect and remove fallen infected leaves.",
                "Keep the area around the tree clean.",
                "Monitor new leaves regularly.",
                "Consider resistant apple varieties."
            ]
        },

        "Apple___Black_rot": {
            "status": "Possible Apple Black Rot",
            "description": "Apple black rot is a fungal disease affecting leaves, fruits and woody parts.",
            "symptoms": [
                "Dark spots on leaves.",
                "Dark rotting areas on fruits.",
                "Cankers on affected branches."
            ],
            "tips": [
                "Remove infected and fallen plant material.",
                "Inspect branches regularly.",
                "Maintain good airflow through proper pruning.",
                "Monitor fruits and leaves."
            ]
        },

        "Apple___Cedar_apple_rust": {
            "status": "Possible Cedar Apple Rust",
            "description": "A fungal disease associated with apple trees and certain juniper hosts.",
            "symptoms": [
                "Yellow or orange spots on leaves.",
                "Spots become more noticeable over time.",
                "Raised structures may appear underneath leaves."
            ],
            "tips": [
                "Monitor leaves during the growing season.",
                "Consider resistant apple varieties.",
                "Inspect nearby susceptible host plants.",
                "Seek local agricultural advice if symptoms persist."
            ]
        },
        "Apple___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the apple leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model.",
                "The leaf should still be inspected for unusual changes."
            ],
            "tips": [
                "Monitor leaves and branches regularly.",
                "Maintain suitable soil moisture.",
                "Provide balanced plant nutrition.",
                "Keep the growing area clean."
            ]
        },

        # BLUEBERRY
        "Blueberry___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the blueberry leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model.",
                "The leaf should still be inspected for unusual changes."
            ],
            "tips": [
                "Maintain suitable soil moisture.",
                "Provide appropriate sunlight and nutrition.",
                "Monitor leaves and branches regularly.",
                "Maintain good growing-area hygiene."
            ]
        },

        # CHERRY
        "Cherry_(including_sour)___Powdery_mildew": {
            "status": "Possible Cherry Powdery Mildew",
            "description": "Powdery mildew is a fungal disease that can affect cherry leaves, shoots and fruit.",
            "symptoms": [
                "White powdery growth on leaves.",
                "White fungal growth on young shoots.",
                "Affected leaves may become distorted.",
                "New growth may be affected more severely."
            ],
            "tips": [
                "Monitor new shoots and leaves regularly.",
                "Maintain good airflow around branches.",
                "Remove severely affected plant material where appropriate.",
                "Seek local agricultural advice for disease management."
            ]
        },

        "Cherry_(including_sour)___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the cherry leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model."
            ],
            "tips": [
                "Monitor leaves and shoots regularly.",
                "Maintain suitable watering.",
                "Keep the growing area clean.",
                "Inspect new growth for unusual changes."
            ]
        },

        # CORN
        "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
            "status": "Possible Corn Gray Leaf Spot",
            "description": "Gray leaf spot is a fungal disease that affects corn foliage.",
            "symptoms": [
                "Small spots may appear on leaves.",
                "Lesions become tan or gray.",
                "Mature lesions often have rectangular shapes.",
                "Lesions may develop parallel to leaf veins."
            ],
            "tips": [
                "Consider resistant corn hybrids.",
                "Practice crop rotation where suitable.",
                "Manage infected crop residue appropriately.",
                "Monitor crops during warm and humid weather."
            ]
        },

        "Corn_(maize)___Common_rust_": {
            "status": "Possible Corn Common Rust",
            "description": "Common rust is a fungal disease caused by Puccinia sorghi.",
            "symptoms": [
                "Reddish-brown elongated pustules on leaves.",
                "Pustules may occur on both leaf surfaces.",
                "Severe infection may cause leaf yellowing."
            ],
            "tips": [
                "Consider resistant corn hybrids.",
                "Monitor leaves for rust-colored pustules.",
                "Inspect crops regularly during humid weather.",
                "Seek local agricultural advice if symptoms increase."
            ]
        },

        "Corn_(maize)___Northern_Leaf_Blight": {
            "status": "Possible Northern Corn Leaf Blight",
            "description": "Northern corn leaf blight is a fungal disease caused by Exserohilum turcicum.",
            "symptoms": [
                "Long cigar-shaped lesions on leaves.",
                "Lesions may appear gray-green or tan.",
                "Symptoms often begin on lower leaves.",
                "Lesions may spread towards upper leaves."
            ],
            "tips": [
                "Consider resistant corn hybrids.",
                "Practice suitable crop rotation.",
                "Manage infected crop residue.",
                "Monitor crops during wet and humid weather."
            ]
        },

        "Corn_(maize)___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the corn leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model."
            ],
            "tips": [
                "Monitor leaves regularly.",
                "Maintain balanced soil nutrition.",
                "Provide suitable irrigation.",
                "Keep the growing area free from unnecessary plant debris."
            ]
        },

        
        # GRAPE
        "Grape___Black_rot": {
            "status": "Possible Grape Black Rot",
            "description": "Black rot is a fungal disease affecting grape leaves, shoots and berries.",
            "symptoms": [
                "Brown circular spots may appear on leaves.",
                "Dark borders may develop around leaf spots.",
                "Infected berries may shrivel and become dark."
            ],
            "tips": [
                "Remove infected berries and plant debris.",
                "Monitor leaves and fruits regularly.",
                "Maintain good airflow around grapevines.",
                "Seek local agricultural advice for disease management."
            ]
        },

        "Grape___Esca_(Black_Measles)": {
            "status": "Possible Grape Esca",
            "description": "Esca is a complex grapevine disease associated with fungal pathogens.",
            "symptoms": [
                "Discoloration may appear between leaf veins.",
                "Leaves may develop striped or scorched patterns.",
                "Berries may develop dark spots."
            ],
            "tips": [
                "Inspect grapevines regularly.",
                "Avoid unnecessary injuries during pruning.",
                "Remove severely affected plant material appropriately.",
                "Consult a grape-growing specialist for management."
            ]
        },

        "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
            "status": "Possible Grape Leaf Blight",
            "description": "Grape leaf blight is a fungal disease that affects grape foliage.",
            "symptoms": [
                "Brown or dark spots may appear on leaves.",
                "Spots may enlarge over time.",
                "Severely affected leaves may dry out."
            ],
            "tips": [
                "Remove fallen infected leaves.",
                "Maintain good airflow around vines.",
                "Monitor foliage during humid weather.",
                "Seek local agricultural advice if symptoms spread."
            ]
        },

        "Grape___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the grape leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model."
            ],
            "tips": [
                "Monitor leaves and fruits regularly.",
                "Maintain suitable irrigation.",
                "Provide balanced plant nutrition.",
                "Keep the vineyard clean."
            ]
        },

        # ORANGE
        "Orange___Haunglongbing_(Citrus_greening)": {
            "status": "Possible Citrus Greening",
            "description": "Citrus greening, also called Huanglongbing (HLB), is a serious bacterial disease affecting citrus trees.",
            "symptoms": [
                "Uneven yellowing of leaves.",
                "Yellow shoots may develop.",
                "Fruits may become small or misshapen.",
                "Fruit colour may develop unevenly."
            ],
            "tips": [
                "Monitor citrus trees for unusual leaf patterns.",
                "Use certified disease-free planting material.",
                "Control the insect vector through locally recommended methods.",
                "Contact agricultural authorities if symptoms are suspected."
            ]
        },

        # PEACH
        "Peach___Bacterial_spot": {
            "status": "Possible Peach Bacterial Spot",
            "description": "Bacterial spot is a disease affecting peach leaves and fruits.",
            "symptoms": [
                "Small dark spots may appear on leaves.",
                "Leaf spots may develop yellow areas around them.",
                "Affected leaves may develop holes or fall.",
                "Fruit may develop dark, sunken spots."
            ],
            "tips": [
                "Use suitable resistant varieties where available.",
                "Avoid unnecessary wetting of foliage.",
                "Remove severely infected plant material appropriately.",
                "Seek local agricultural advice for disease management."
            ]
        },

        "Peach___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the peach leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model."
            ],
            "tips": [
                "Monitor leaves and fruits regularly.",
                "Maintain suitable watering.",
                "Provide balanced plant nutrition.",
                "Keep the growing area clean."
            ]
        },

        # BELL PEPPER
        "Pepper,_bell___Bacterial_spot": {
            "status": "Possible Bell Pepper Bacterial Spot",
            "description": "Bacterial spot is a plant disease that affects pepper leaves and fruits.",
            "symptoms": [
                "Small water-soaked spots may appear on leaves.",
                "Spots may become dark and irregular.",
                "Yellowing may develop around leaf spots.",
                "Fruit may develop raised or rough spots."
            ],
            "tips": [
                "Use disease-free seeds and seedlings.",
                "Avoid working with wet plants.",
                "Remove infected plant debris.",
                "Use locally recommended disease-management practices."
            ]
        },

        "Pepper,_bell___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the bell pepper leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model."
            ],
            "tips": [
                "Monitor leaves regularly.",
                "Maintain suitable irrigation.",
                "Provide balanced plant nutrition.",
                "Keep the growing area clean."
            ]
        },

        # POTATO
        "Potato___Early_blight": {
            "status": "Possible Potato Early Blight",
            "description": "Early blight is a fungal disease caused by Alternaria solani. It commonly affects potato leaves.",
            "symptoms": [
                "Dark brown spots may appear on older leaves.",
                "Spots may develop concentric rings.",
                "Yellowing may occur around affected areas.",
                "Severely affected leaves may dry out."
            ],
            "tips": [
                "Use healthy and disease-free planting material.",
                "Practice suitable crop rotation.",
                "Remove infected plant debris.",
                "Monitor older leaves regularly."
            ]
        },

        "Potato___Late_blight": {
            "status": "Possible Potato Late Blight",
            "description": "Late blight is a serious potato disease caused by the pathogen Phytophthora infestans.",
            "symptoms": [
                "Water-soaked spots may appear on leaves.",
                "Dark lesions may develop on leaf surfaces.",
                "White fungal-like growth may appear underneath leaves in humid conditions.",
                "Infected tubers may develop brown rot."
            ],
            "tips": [
                "Use certified disease-free seed potatoes.",
                "Monitor crops during cool and wet weather.",
                "Remove infected plant material appropriately.",
                "Seek local agricultural advice if late blight is suspected."
            ]
        },

        "Potato___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the potato leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model."
            ],
            "tips": [
                "Monitor leaves regularly.",
                "Maintain suitable irrigation.",
                "Provide balanced soil nutrition.",
                "Use healthy planting material."
            ]
        },

        # RASPBERRY
        "Raspberry___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the raspberry leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model."
            ],
            "tips": [
                "Monitor leaves and stems regularly.",
                "Maintain suitable soil moisture.",
                "Provide appropriate sunlight.",
                "Keep the growing area clean."
            ]
        },

        # SOYBEAN
        "Soybean___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the soybean leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model."
            ],
            "tips": [
                "Monitor leaves regularly.",
                "Maintain suitable irrigation.",
                "Provide balanced plant nutrition.",
                "Inspect plants for unusual changes."
            ]
        },

        # SQUASH
        "Squash___Powdery_mildew": {
            "status": "Possible Squash Powdery Mildew",
            "description": "Powdery mildew is a fungal disease that commonly affects squash leaves and stems.",
            "symptoms": [
                "White powder-like patches may appear on leaves.",
                "White growth may spread across leaf surfaces.",
                "Affected leaves may turn yellow.",
                "Severely affected leaves may dry out."
            ],
            "tips": [
                "Monitor leaves regularly.",
                "Maintain suitable spacing between plants.",
                "Remove severely affected plant material appropriately.",
                "Use locally recommended disease-management practices."
            ]
        },

        # STRAWBERRY
        "Strawberry___Leaf_scorch": {
            "status": "Possible Strawberry Leaf Scorch",
            "description": "Leaf scorch is a fungal disease caused by Diplocarpon earlianum that affects strawberry foliage.",
            "symptoms": [
                "Small dark purple or reddish spots on leaves.",
                "Spots may enlarge and develop brown centres.",
                "Affected leaf areas may become dry and scorched.",
                "Severely affected leaves may die."
            ],
            "tips": [
                "Remove infected and fallen leaves.",
                "Maintain good airflow between plants.",
                "Avoid unnecessary wetting of foliage.",
                "Monitor plants regularly during humid weather."
            ]
        },

        "Strawberry___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the strawberry leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model."
            ],
            "tips": [
                "Monitor leaves and fruits regularly.",
                "Maintain suitable soil moisture.",
                "Provide balanced plant nutrition.",
                "Keep the growing area clean."
            ]
        },

        # TOMATO
        "Tomato___Bacterial_spot": {
            "status": "Possible Tomato Bacterial Spot",
            "description": "Bacterial spot is a disease affecting tomato leaves, stems and fruits.",
            "symptoms": [
                "Small dark spots on leaves.",
                "Yellow areas may develop around spots.",
                "Dark raised spots may appear on fruits.",
                "Severe infection may cause leaf drop."
            ],
            "tips": [
                "Use disease-free seeds and seedlings.",
                "Avoid handling plants when foliage is wet.",
                "Remove infected plant debris.",
                "Maintain good field hygiene."
            ]
        },

        "Tomato___Early_blight": {
            "status": "Possible Tomato Early Blight",
            "description": "Early blight is a fungal disease caused by Alternaria species.",
            "symptoms": [
                "Dark brown spots on older leaves.",
                "Concentric ring patterns inside lesions.",
                "Yellowing around affected leaf areas.",
                "Affected leaves may dry and fall."
            ],
            "tips": [
                "Remove infected plant debris.",
                "Practice suitable crop rotation.",
                "Avoid unnecessary overhead watering.",
                "Monitor older leaves regularly."
            ]
        },

        "Tomato___Late_blight": {
            "status": "Possible Tomato Late Blight",
            "description": "Late blight is a serious disease caused by Phytophthora infestans.",
            "symptoms": [
                "Water-soaked leaf patches.",
                "Dark brown or black lesions.",
                "White growth may appear underneath leaves in humid conditions.",
                "Fruits may develop firm brown areas."
            ],
            "tips": [
                "Use healthy planting material.",
                "Monitor plants during cool and wet weather.",
                "Remove infected plant material appropriately.",
                "Seek agricultural advice promptly if suspected."
            ]
        },

        "Tomato___Leaf_Mold": {
            "status": "Possible Tomato Leaf Mold",
            "description": "Leaf mold is a fungal disease commonly associated with humid growing conditions.",
            "symptoms": [
                "Pale green or yellow patches on upper leaf surfaces.",
                "Olive-green or grayish growth underneath leaves.",
                "Affected leaves may curl.",
                "Severe infection may cause leaf drying."
            ],
            "tips": [
                "Improve airflow around plants.",
                "Avoid excessive humidity.",
                "Water near the soil rather than wetting foliage.",
                "Remove infected plant debris."
            ]
        },

        "Tomato___Septoria_leaf_spot": {
            "status": "Possible Tomato Septoria Leaf Spot",
            "description": "Septoria leaf spot is a fungal disease caused by Septoria lycopersici.",
            "symptoms": [
                "Small circular spots on leaves.",
                "Spots may have gray or tan centres.",
                "Dark borders may surround the spots.",
                "Severe infection may cause lower leaves to fall."
            ],
            "tips": [
                "Remove infected lower leaves where appropriate.",
                "Avoid overhead irrigation.",
                "Practice crop rotation.",
                "Remove infected plant debris."
            ]
        },

        "Tomato___Spider_mites Two-spotted_spider_mite": {
            "status": "Possible Two-Spotted Spider Mite Damage",
            "description": "Two-spotted spider mites are tiny pests that feed on plant leaf cells.",
            "symptoms": [
                "Fine pale speckling on leaves.",
                "Yellow or bronze discoloration.",
                "Fine webbing may appear on leaves.",
                "Severe infestations may cause leaf drying."
            ],
            "tips": [
                "Inspect the undersides of leaves.",
                "Monitor plants regularly for mites.",
                "Protect beneficial predatory insects.",
                "Seek local agricultural advice for suitable pest management."
            ]
        },

        "Tomato___Target_Spot": {
            "status": "Possible Tomato Target Spot",
            "description": "Target spot is a fungal disease associated with Corynespora cassiicola.",
            "symptoms": [
                "Brown circular spots on leaves.",
                "Concentric rings may appear inside lesions.",
                "Lesions may develop yellow margins.",
                "Affected leaves may fall prematurely."
            ],
            "tips": [
                "Maintain good airflow around plants.",
                "Remove infected plant debris.",
                "Avoid unnecessary wetting of foliage.",
                "Monitor plants regularly."
            ]
        },

        "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
            "status": "Possible Tomato Yellow Leaf Curl Virus",
            "description": "Tomato yellow leaf curl is a viral disease commonly transmitted by whiteflies.",
            "symptoms": [
                "Yellowing of leaves.",
                "Upward curling of leaf edges.",
                "Reduced plant growth.",
                "Affected plants may produce fewer fruits."
            ],
            "tips": [
                "Use healthy and virus-free seedlings.",
                "Monitor plants for whiteflies.",
                "Remove severely affected plants following local guidance.",
                "Use locally recommended whitefly management practices."
            ]
        },

        "Tomato___Tomato_mosaic_virus": {
            "status": "Possible Tomato Mosaic Virus",
            "description": "Tomato mosaic virus is a viral disease that can affect tomato growth and foliage.",
            "symptoms": [
                "Light and dark green mosaic patterns on leaves.",
                "Leaf distortion.",
                "Uneven plant growth.",
                "Fruit development may be affected."
            ],
            "tips": [
                "Use certified virus-free seeds.",
                "Maintain clean gardening tools.",
                "Remove infected plants following local guidance.",
                "Avoid handling healthy plants after infected plants without cleaning hands."
            ]
        },

        "Tomato___healthy": {
            "status": "Healthy Category Predicted",
            "description": "The model classified the tomato leaf as healthy.",
            "symptoms": [
                "No disease category was detected by the model."
            ],
            "tips": [
                "Monitor leaves and fruits regularly.",
                "Maintain suitable irrigation.",
                "Provide balanced plant nutrition.",
                "Keep the growing area clean."
            ]
        },



    }

    # Return information for the selected category
    if disease_name in disease_data:
        return disease_data[disease_name]

    # General fallback for other healthy categories
    if "healthy" in disease_name.lower():
        return {
            "status": "Healthy Category Predicted",
            "description": "The model classified this leaf as belonging to a healthy plant category.",
            "symptoms": [
                "No disease category was detected by the model."
            ],
            "tips": [
                "Monitor plants regularly.",
                "Maintain suitable watering and nutrition.",
                "Keep the growing area clean.",
                "Inspect leaves for unusual changes."
            ]
        }

    # General fallback for categories not added yet
    return {
        "status": "Possible Disease Detected",
        "description": (
            "The model predicted: "
            + disease_name.replace("___", " - ").replace("_", " ")
            + ". Detailed information for this category will be added."
        ),
        "symptoms": [
            "Further inspection is required to confirm symptoms."
        ],
        "tips": [
            "Monitor the affected plant.",
            "Maintain good field hygiene.",
            "Seek advice from an agricultural expert."
        ]
    }
