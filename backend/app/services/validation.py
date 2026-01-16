# backend/app/services/validation.py

def validate_slab(thickness_m, steel_kg_m3):
    issues = []

    if thickness_m < 0.08:
        issues.append({
            "severity": "ERROR",
            "message": "Espesor de losa menor a 8 cm (NO CUMPLE)"
        })

    if steel_kg_m3 < 70:
        issues.append({
            "severity": "WARNING",
            "message": "Cuantía de acero baja para losa"
        })

    return issues
