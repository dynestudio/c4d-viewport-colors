import colorsys

DEG30 = 30/360.
def adjacent_colors((r, g, b), d=DEG30): # Assumption: r, g, b in [0, 255]
    r, g, b = map(lambda x: x/255., [r, g, b]) # Convert to [0, 1]
    h, l, s = colorsys.rgb_to_hls(r, g, b)     # RGB -> HLS
    h = [(h+d) % 1 for d in (-d, d)]           # Rotation by d
    adjacent = [map(lambda x: int(round(x*255)), colorsys.hls_to_rgb(hi, l, s))
            for hi in h] # H'LS -> new RGB
    return adjacent