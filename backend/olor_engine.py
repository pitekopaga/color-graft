import numpy as np
from enum import Enum

class CVDType(Enum):
    PROTAN = "protan"      # red-deficient
    DEUTAN = "deutan"      # green-deficient  
    TRITAN = "tritan"      # blue-deficient

def cvd_transform(rgb, cvd_type: CVDType, severity: float):
    """
    rgb: tuple of (r,g,b) values 0-255
    cvd_type: PROTAN, DEUTAN, or TRITAN
    severity: 0.0 to 1.0 (0 = normal vision, 1 = complete deficiency)
    """
    # Convert to 0-1 range
    r, g, b = rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0
    
    if cvd_type == CVDType.PROTAN:
        # Shift red toward blue/green based on severity
        r_shifted = r * (1 - severity) + g * severity * 0.5 + b * severity * 0.5
        g_shifted = g
        b_shifted = b
    elif cvd_type == CVDType.DEUTAN:
        # Shift green toward red/blue
        r_shifted = r
        g_shifted = g * (1 - severity) + r * severity * 0.6 + b * severity * 0.4
        b_shifted = b
    elif cvd_type == CVDType.TRITAN:
        # Shift blue toward green/red
        r_shifted = r
        g_shifted = g
        b_shifted = b * (1 - severity) + g * severity * 0.7 + r * severity * 0.3
    else:
        return rgb
    
    # Clamp and convert back to 0-255
    return (int(max(0, min(255, r_shifted * 255))),
            int(max(0, min(255, g_shifted * 255))),
            int(max(0, min(255, b_shifted * 255))))

def transform_palette(palette, cvd_type, severity):
    """Apply transformation to entire color palette"""
    return [cvd_transform(color, cvd_type, severity) for color in palette]
