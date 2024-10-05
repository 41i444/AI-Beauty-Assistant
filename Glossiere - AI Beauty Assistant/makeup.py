# makeup.py

def get_makeup_looks(face_shape):
    makeup_looks = {
        "oval": [
            ("Natural 'No-Makeup' Makeup", "Enhances natural beauty with minimal products for a fresh look.", "images/natural_makeup.jpg"),
            ("Soft Glam", "Features blended eyeshadows and soft lip colors for a polished yet subtle effect.", "images/soft_glam.jpg"),
            ("Dewy, Glowy Skin", "Showcases symmetry with a luminous base and highlights.", "images/dewy_glow.jpg"),
            ("Classic Retro", "Bold eyeliner and red lips accentuate the elegance of the oval shape.", "images/classic_retro.jpg")
        ],
        "square": [
            ("Soft Glam", "Softly blended eyeshadows and rounded eyeliner help soften angles.", "images/soft_glam.jpg"),
            ("Classic Retro", "Softens the jawline with contouring, using rounded eyeliner.", "images/classic_retro.jpg"),
            ("Smokey Eye", "Dramatic eyes with a softer lip color to draw attention away from the angles.", "images/smokey_eye.jpg"),
            ("Thai Makeup", "Bright colors bring out features while contouring softens the jawline.", "images/thai_makeup.jpg")
        ],
        "round": [
            ("Arabic Makeup", "Elongates the face with contouring and bold eye makeup.", "images/arabic_makeup.jpg"),
            ("Smokey Eye", "Adds depth and elongation with strong contouring.", "images/smokey_eye.jpg"),
            ("Dewy, Glowy Skin", "Highlights cheekbones for a sculpted appearance.", "images/dewy_glow.jpg"),
            ("Soft Glam", "Soft colors that add dimension without overwhelming roundness.", "images/soft_glam.jpg")
        ]
    }

    if face_shape.lower() in makeup_looks:
        return makeup_looks[face_shape.lower()]
    else:
        return None