# data_dict.py

data_dict = {
    # Apple
    "Apple___Apple_scab": {
        "disease_name": "Apple Scab",
        "plant": "Apple",
        "symptoms": "Dark, scabby lesions on leaves and fruit; leaf curling and yellowing.",
        "causes": "Fungus Venturia inaequalis; spreads in wet, cool conditions.",
        "remedies": "Prune infected areas, apply fungicides (e.g. Captan or Mancozeb), ensure good air circulation.",
        "sample_image_path": "train/Apple___Apple_scab/"
    },
    "Apple___Black_rot": {
        "disease_name": "Black Rot",
        "plant": "Apple",
        "symptoms": "Circular dark spots on leaves, rotting fruit, branch cankers.",
        "causes": "Fungus Botryosphaeria obtusa.",
        "remedies": "Remove infected debris, prune branches, use appropriate fungicides.",
        "sample_image_path": "train/Apple___Black_rot/"
    },
    "Apple___Cedar_apple_rust": {
        "disease_name": "Cedar Apple Rust",
        "plant": "Apple",
        "symptoms": "Bright orange-yellow spots on leaves; lesions on fruit and twigs.",
        "causes": "Gymnosporangium fungal species transmitted from junipers.",
        "remedies": "Remove nearby juniper hosts, prune infected foliage, apply rust‑control fungicides.",
        "sample_image_path": "train/Apple___Cedar_apple_rust/"
    },
    "Apple___healthy": {
        "disease_name": "Healthy Apple",
        "plant": "Apple",
        "symptoms": "Leaves and fruit clean; no visible lesions.",
        "causes": "—",
        "remedies": "Maintain balanced care, pruning, moisture control.",
        "sample_image_path": "train/Apple___healthy/"
    },

    # Blueberry
    "Blueberry___healthy": {
        "disease_name": "Healthy Blueberry",
        "plant": "Blueberry",
        "symptoms": "Leaves uniform green; fruit intact.",
        "causes": "—",
        "remedies": "Proper watering, pruning, disease monitoring.",
        "sample_image_path": "train/Blueberry___healthy/"
    },

    # Cherry
    "Cherry_(including_sour)___Powdery_mildew": {
        "disease_name": "Cherry Powdery Mildew",
        "plant": "Cherry",
        "symptoms": "White-gray powdery coating on leaves and young shoots.",
        "causes": "Fungus Erysiphales species; thrives in humid, shaded conditions.",
        "remedies": "Improve air flow, prune infected parts, apply sulfur or neem oil fungicides.",
        "sample_image_path": "train/Cherry_(including_sour)___Powdery_mildew/"
    },
    "Cherry_(including_sour)___healthy": {
        "disease_name": "Healthy Cherry",
        "plant": "Cherry",
        "symptoms": "Green leaves, no spots; fruit well‑formed.",
        "causes": "—",
        "remedies": "Standard care, pruning, pest control.",
        "sample_image_path": "train/Cherry_(including_sour)___healthy/"
    },

    # Corn
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "disease_name": "Gray Leaf Spot",
        "plant": "Corn",
        "symptoms": "Gray to tan lesions with distinct rectangular edges on leaves.",
        "causes": "Cercospora zeae-maydis fungus.",
        "remedies": "Rotate crops, remove residue, fungicide sprays.",
        "sample_image_path": "train/Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot/"
    },
    "Corn_(maize)___Common_rust_": {
        "disease_name": "Common Rust",
        "plant": "Corn",
        "symptoms": "Small reddish-brown pustules on leaf surfaces.",
        "causes": "Puccinia sorghi fungus.",
        "remedies": "Plant resistant varieties, apply fungicides, crop rotation.",
        "sample_image_path": "train/Corn_(maize)___Common_rust_/"
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "disease_name": "Northern Leaf Blight",
        "plant": "Corn",
        "symptoms": "Long, elliptical gray-green lesions on leaves.",
        "causes": "Exserohilum turcicum fungus.",
        "remedies": "Use resistant hybrids, rotate fields, apply foliar fungicides.",
        "sample_image_path": "train/Corn_(maize)___Northern_Leaf_Blight/"
    },
    "Corn_(maize)___healthy": {
        "disease_name": "Healthy Corn",
        "plant": "Corn",
        "symptoms": "Uniform green leaves; no lesions.",
        "causes": "—",
        "remedies": "Balanced fertilizer, pest monitoring, irrigation.",
        "sample_image_path": "train/Corn_(maize)___healthy/"
    },

    # Grape
    "Grape___Black_rot": {
        "disease_name": "Grape Black Rot",
        "plant": "Grape",
        "symptoms": "Black circular spots on leaves and fruit developing into shriveled mummies.",
        "causes": "Guignardia bidwellii fungus.",
        "remedies": "Remove mummified fruit, spray fungicides, ensure canopy ventilation.",
        "sample_image_path": "train/Grape___Black_rot/"
    },
    "Grape___Esca_(Black_Measles)": {
        "disease_name": "Grape Black Measles",
        "plant": "Grape",
        "symptoms": "Dark lesions on berries; sometimes with pink halos.",
        "causes": "Didymella bryoniae / Phomopsis viticola fungi.",
        "remedies": "Prune and remove infected canes, apply fungicides, use disease‑free stock.",
        "sample_image_path": "train/Grape___Esca_(Black_Measles)/"
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "disease_name": "Grape Leaf Blight",
        "plant": "Grape",
        "symptoms": "Brown spots with yellow halos on leaves.",
        "causes": "Phomopsis viticola fungus.",
        "remedies": "Prune and destroy infected shoots, spray fungicides, maintain airflow.",
        "sample_image_path": "train/Grape___Leaf_blight_(Isariopsis_Leaf_Spot)/"
    },
    "Grape___healthy": {
        "disease_name": "Healthy Grape",
        "plant": "Grape",
        "symptoms": "Leaves green and unblemished; fruit healthy.",
        "causes": "—",
        "remedies": "Train vines for air circulation, prune debris removal.",
        "sample_image_path": "train/Grape___healthy/"
    },

    # Orange
    "Orange___Haunglongbing_(Citrus_greening)": {
        "disease_name": "Huanglongbing (Citrus Greening)",
        "plant": "Orange",
        "symptoms": "Yellow shoots, mottled leaves, small bitter fruit, branch dieback.",
        "causes": "Bacterium Candidatus Liberibacter transmitted by psyllids.",
        "remedies": "Remove infected trees, control psyllid vector, use disease‑free stock.",
        "sample_image_path": "train/Orange___Haunglongbing_(Citrus_greening)/"
    },

    # Bell Pepper
    "Pepper,_bell___Bacterial_spot": {
        "disease_name": "Bell Pepper Bacterial Spot",
        "plant": "Bell Pepper",
        "symptoms": "Dark water‑soaked spots on leaves and fruit.",
        "causes": "Xanthomonas campestris bacteria.",
        "remedies": "Use disease‑free seed, apply copper sprays, rotate crops.",
        "sample_image_path": "train/Pepper,_bell___Bacterial_spot/"
    },
    "Pepper,_bell___healthy": {
        "disease_name": "Healthy Bell Pepper",
        "plant": "Bell Pepper",
        "symptoms": "Leaves and fruit healthy.",
        "causes": "—",
        "remedies": "Maintain normal care, insect and disease monitoring.",
        "sample_image_path": "train/Pepper,_bell___healthy/"
    },

    # Potato
    "Potato___Early_blight": {
        "disease_name": "Potato Early Blight",
        "plant": "Potato",
        "symptoms": "Target-like concentric rings on older leaves.",
        "causes": "Alternaria solani fungus.",
        "remedies": "Remove affected leaves, crop rotation, apply fungicides.",
        "sample_image_path": "train/Potato___Early_blight/"
    },
    "Potato___Late_blight": {
        "disease_name": "Potato Late Blight",
        "plant": "Potato",
        "symptoms": "Water-soaked lesions that darken and expand; white mold under leaves.",
        "causes": "Phytophthora infestans pathogen.",
        "remedies": "Destroy infected plants, apply copper fungicides, improve drainage.",
        "sample_image_path": "train/Potato___Late_blight/"
    },
    "Potato___healthy": {
        "disease_name": "Healthy Potato",
        "plant": "Potato",
        "symptoms": "Normal leaves, firm tubers.",
        "causes": "—",
        "remedies": "Balanced irrigation, fertilization, pest monitoring.",
        "sample_image_path": "train/Potato___healthy/"
    },

    # Raspberry
    "Raspberry___healthy": {
        "disease_name": "Healthy Raspberry",
        "plant": "Raspberry",
        "symptoms": "Uniform green foliage; clean fruit.",
        "causes": "—",
        "remedies": "Good pruning, pest and disease control.",
        "sample_image_path": "train/Raspberry___healthy/"
    },

    # Soybean
    "Soybean___healthy": {
        "disease_name": "Healthy Soybean",
        "plant": "Soybean",
        "symptoms": "Green trifoliate leaves; no lesions.",
        "causes": "—",
        "remedies": "Maintain crop rotation and disease monitoring.",
        "sample_image_path": "train/Soybean___healthy/"
    },

    # Squash
    "Squash___Powdery_mildew": {
        "disease_name": "Squash Powdery Mildew",
        "plant": "Squash",
        "symptoms": "White-gray powdery spots on leaves and stems, leading to yellowing and browning.",
        "causes": "Fungi (e.g. Podosphaera fuliginea, Erysiphe cichoracearum).",
        "remedies": "Increase spacing, improve air circulation, remove infected leaves, apply sulfur, neem oil or baking soda/oil sprays weekly.",
        "sample_image_path": "train/Squash___Powdery_mildew/"
    },

    # Strawberry
    "Strawberry___Leaf_scorch": {
        "disease_name": "Strawberry Leaf Scorch",
        "plant": "Strawberry",
        "symptoms": "Brown edges and blotches on leaves, often between veins.",
        "causes": "Xanthomonas fragariae bacteria.",
        "remedies": "Remove infected foliage, avoid overhead watering, apply copper-based sprays.",
        "sample_image_path": "train/Strawberry___Leaf_scorch/"
    },
    "Strawberry___healthy": {
        "disease_name": "Healthy Strawberry",
        "plant": "Strawberry",
        "symptoms": "Green leaves, healthy fruit.",
        "causes": "—",
        "remedies": "Proper mulch, watering, disease control.",
        "sample_image_path": "train/Strawberry___healthy/"
    },

    # Tomato
    "Tomato___Bacterial_spot": {
        "disease_name": "Tomato Bacterial Spot",
        "plant": "Tomato",
        "symptoms": "Small, dark water-soaked spots on leaves and fruit.",
        "causes": "Xanthomonas species bacterium.",
        "remedies": "Use certified seeds, copper sprays, crop rotation.",
        "sample_image_path": "train/Tomato___Bacterial_spot/"
    },
    "Tomato___Early_blight": {
        "disease_name": "Tomato Early Blight",
        "plant": "Tomato",
        "symptoms": "Concentric ring spots on older leaves.",
        "causes": "Alternaria solani fungus.",
        "remedies": "Remove affected leaves, rotate crops, fungicides such as chlorothalonil.",
        "sample_image_path": "train/Tomato___Early_blight/"
    },
    "Tomato___Late_blight": {
        "disease_name": "Tomato Late Blight",
        "plant": "Tomato",
        "symptoms": "Brown lesions with pale borders on leaves; fruit rot, stem lesions.",
        "causes": "Phytophthora infestans; thrives in humid conditions.",
        "remedies": "Remove infected plants, avoid overhead watering, copper-based fungicides.",
        "sample_image_path": "train/Tomato___Late_blight/"
    },
    "Tomato___Leaf_Mold": {
        "disease_name": "Tomato Leaf Mold",
        "plant": "Tomato",
        "symptoms": "Yellow spots on top leaf surface; olive-green fuzzy mold underneath.",
        "causes": "Passalora fulva fungus.",
        "remedies": "Improve air circulation, reduce humidity, apply chlorothalonil fungicide.",
        "sample_image_path": "train/Tomato___Leaf_Mold/"
    },
    "Tomato___Septoria_leaf_spot": {
        "disease_name": "Tomato Septoria Leaf Spot",
        "plant": "Tomato",
        "symptoms": "Small circular spots with dark borders and gray centers on lower leaves.",
        "causes": "Septoria lycopersici fungus.",
        "remedies": "Remove lower leaves, apply copper or chlorothalonil fungicides, space plants.",
        "sample_image_path": "train/Tomato___Septoria_leaf_spot/"
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "disease_name": "Tomato Two‑Spotted Spider Mite",
        "plant": "Tomato",
        "symptoms": "Tiny yellow or white speckles on leaves; fine webbing.",
        "causes": "Tetranychus urticae mites.",
        "remedies": "Wash plants, use miticides or insecticidal soaps, increase humidity.",
        "sample_image_path": "train/Tomato___Spider_mites Two-spotted_spider_mite/"
    },
    "Tomato___Target_Spot": {
        "disease_name": "Tomato Target Spot",
        "plant": "Tomato",
        "symptoms": "Dark lesions on leaves with concentric rings and yellow halos.",
        "causes": "Corynespora cassiicola fungus.",
        "remedies": "Prune diseased foliage, apply appropriate fungicides, maintain drainage.",
        "sample_image_path": "train/Tomato___Target_Spot/"
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "disease_name": "Tomato Yellow Leaf Curl Virus",
        "plant": "Tomato",
        "symptoms": "Leaves curl upward and yellow; stunted plants and poor fruit set.",
        "causes": "Begomovirus spread by whiteflies.",
        "remedies": "Use resistant cultivars, control whiteflies, remove infected plants.",
        "sample_image_path": "train/Tomato___Tomato_Yellow_Leaf_Curl_Virus/"
    },
    "Tomato___Tomato_mosaic_virus": {
        "disease_name": "Tomato Mosaic Virus",
        "plant": "Tomato",
        "symptoms": "Mottled yellow and dark-green foliage; fern-like deformed leaves; stunting; uneven fruit ripening.",
        "causes": "Tomato mosaic virus (ToMV); virus persists on seed, tools, hands; spread via contact or seed.",
        "remedies": "Use resistant varieties and certified virus-free seed; disinfect tools and hands; remove and burn infected plants; rotate crops.",
        "sample_image_path": "train/Tomato___Tomato_mosaic_virus/"
    },
    "Tomato___healthy": {
        "disease_name": "Healthy Tomato",
        "plant": "Tomato",
        "symptoms": "Green, uniform leaves; clean, well-formed fruit.",
        "causes": "—",
        "remedies": "Provide balanced nutrients, watering, sunlight, and pest management.",
        "sample_image_path": "train/Tomato___healthy/"
    }
}


def get_disease_details(class_name):
    return data_dict.get(class_name, {
        "disease_name": "Unknown",
        "plant": "Unknown",
        "symptoms": "No data available.",
        "causes": "No data available.",
        "remedies": "No remedies available.",
        "sample_image_path": ""
    })
