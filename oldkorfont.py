class GlyphDesigner:
    def __init__(self, font):
        self.font = font
        self.em_size = 1000  # Standard em square size
        
    def design_base_glyph(self, unicode_value: int, paths: List[Dict]):
        """Create a base glyph from path definitions"""
        glyph = self.font.createChar(unicode_value)
        pen = glyph.glyphPen()
        
        for path in paths:
            pen.moveTo(path['start'])
            
            for command in path['commands']:
                if command['type'] == 'lineTo':
                    pen.lineTo(command['point'])
                elif command['type'] == 'curveTo':
                    pen.curveTo(command['control1'], 
                              command['control2'], 
                              command['point'])
                elif command['type'] == 'qcurveTo':
                    pen.qcurveTo(command['control'], 
                               command['point'])
        
        pen.closePath()
        return glyph
    
    def create_vowel_glyph(self, unicode_value: int, vowel_type: str):
        """Create vowel glyphs with specific characteristics"""
        glyph = self.font.createChar(unicode_value)
        
        if vowel_type == "vertical":
            # Create vertical vowel stroke
            self._create_vertical_stroke(glyph)
        elif vowel_type == "horizontal":
            # Create horizontal vowel stroke
            self._create_horizontal_stroke(glyph)
        elif vowel_type == "compound":
            # Create compound vowel combining both strokes
            self._create_compound_stroke(glyph)
            
        return glyph
    
    def create_consonant_glyph(self, unicode_value: int, strokes: List[Dict]):
        """Create consonant glyphs from stroke definitions"""
        glyph = self.font.createChar(unicode_value)
        
        for stroke in strokes:
            self._add_stroke(glyph, stroke)
            
        return glyph
    
    def _create_vertical_stroke(self, glyph):
        """Create a vertical stroke for vowels"""
        pen = glyph.glyphPen()
        # Define vertical stroke geometry
        width = self.em_size * 0.1
        height = self.em_size * 0.8
        x = (self.em_size - width) / 2
        y = (self.em_size - height) / 2
        
        pen.moveTo((x, y))
        pen.lineTo((x + width, y))
        pen.lineTo((x + width, y + height))
        pen.lineTo((x, y + height))
        pen.closePath()
    
    def _create_horizontal_stroke(self, glyph):
        """Create a horizontal stroke for vowels"""
        pen = glyph.glyphPen()
        # Define horizontal stroke geometry
        width = self.em_size * 0.8
        height = self.em_size * 0.1
        x = (self.em_size - width) / 2
        y = (self.em_size - height) / 2
        
        pen.moveTo((x, y))
        pen.lineTo((x + width, y))
        pen.lineTo((x + width, y + height))
        pen.lineTo((x, y + height))
        pen.closePath()
    
    def _create_compound_stroke(self, glyph):
        """Create a compound stroke combining vertical and horizontal"""
        self._create_vertical_stroke(glyph)
        self._create_horizontal_stroke(glyph)
    
    def _add_stroke(self, glyph, stroke_def):
        """Add a stroke to a glyph based on stroke definition"""
        pen = glyph.glyphPen()
        
        # Start point
        pen.moveTo(stroke_def['start'])
        
        # Add curve points if defined
        if 'curve_points' in stroke_def:
            for point in stroke_def['curve_points']:
                if 'control1' in point and 'control2' in point:
                    pen.curveTo(point['control1'], 
                              point['control2'], 
                              point['end'])
                else:
                    pen.lineTo(point['end'])
        
        # End point
        pen.lineTo(stroke_def['end'])
        pen.closePath()

    def apply_transformations(self, glyph, transformations):
        """Apply transformations to a glyph"""
        for transform in transformations:
            if transform['type'] == 'scale':
                glyph.transform(psMat.scale(transform['x'], transform['y']))
            elif transform['type'] == 'rotate':
                glyph.transform(psMat.rotate(math.radians(transform['angle'])))
            elif transform['type'] == 'translate':
                glyph.transform(psMat.translate(transform['x'], transform['y']))

# Example usage:
def create_complex_glyph(font, unicode_value, strokes, transformations=None):
    designer = GlyphDesigner(font)
    glyph = designer.create_consonant_glyph(unicode_value, strokes)
    
    if transformations:
        designer.apply_transformations(glyph, transformations)
    
    return glyph
