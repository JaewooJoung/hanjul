import fontforge
import psMat
import math
from typing import List, Dict, Tuple

class OldKoreanFontForge:
    def __init__(self, font_name: str = "OldKoreanComplete"):
        self.font = fontforge.font()
        self.font.fontname = font_name
        self.font.familyname = font_name
        self.font.fullname = f"{font_name} Regular"
        self.PUA_START = 0xE000  # Private Use Area starting point
        
        # Load character definitions
        self.load_character_definitions()
        
    def load_character_definitions(self):
        # Character definitions from our previous dictionary
        self.old_korean = {
            "initial_consonants": [
                "ᄀ", "ᄁ", "ᄂ", "ᄃ", "ᄄ", "ᄅ", "ᄆ", "ᄇ", "ᄈ", "ᄉ", "ᄊ", "ᄋ",
                "ᄌ", "ᄍ", "ᄎ", "ᄏ", "ᄐ", "ᄑ", "ᄒ", "ㆁ", "ㆆ", "ㅿ"
            ],
            "vowels": [
                "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ",
                "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ", "ㆍ", "ᆢ"
            ],
            "final_consonants": [
                "ᆨ", "ᆩ", "ᆪ", "ᆫ", "ᆬ", "ᆭ", "ᆮ", "ᆯ", "ᆰ", "ᆱ", "ᆲ", "ᆳ", "ᆴ",
                "ᆵ", "ᆶ", "ᆷ", "ᆸ", "ᆹ", "ᆺ", "ᆻ", "ᆼ", "ᆽ", "ᆾ", "ᆿ", "ᇀ", "ᇁ", "ᇂ"
            ]
        }
        
    def create_base_glyphs(self):
        """Create all base glyphs for initial consonants, vowels, and final consonants"""
        for category in ["initial_consonants", "vowels", "final_consonants"]:
            for char in self.old_korean[category]:
                glyph = self.font.createChar(ord(char))
                # Set basic glyph properties
                glyph.width = 1000
                glyph.vwidth = 1000
                
    def calculate_syllable_position(self, initial: str, vowel: str, final: str = None) -> Tuple[int, int, int]:
        """Calculate the position of components in a syllable block"""
        # Basic positioning logic - can be customized based on specific rules
        initial_pos = (100, 600)  # Top position
        vowel_pos = (400, 400)    # Middle position
        final_pos = (250, 100)    # Bottom position if final consonant exists
        
        return initial_pos, vowel_pos, final_pos
    
    def create_syllable_block(self, initial: str, vowel: str, final: str = None) -> int:
        """Create a syllable block and return its Unicode code point"""
        # Calculate unique code point for this combination
        code_point = self.get_syllable_code_point(initial, vowel, final)
        
        # Create new glyph
        glyph = self.font.createChar(code_point)
        
        # Get component positions
        initial_pos, vowel_pos, final_pos = self.calculate_syllable_position(initial, vowel, final)
        
        # Add references to component glyphs
        glyph.addReference(initial, psMat.translate(initial_pos[0], initial_pos[1]))
        glyph.addReference(vowel, psMat.translate(vowel_pos[0], vowel_pos[1]))
        
        if final:
            glyph.addReference(final, psMat.translate(final_pos[0], final_pos[1]))
        
        return code_point
    
    def get_syllable_code_point(self, initial: str, vowel: str, final: str = None) -> int:
        """Calculate unique code point for syllable combination"""
        initial_index = self.old_korean["initial_consonants"].index(initial)
        vowel_index = self.old_korean["vowels"].index(vowel)
        final_index = self.old_korean["final_consonants"].index(final) if final else 0
        
        # Create unique code point in Private Use Area
        return self.PUA_START + (initial_index * 23 * 27) + (vowel_index * 27) + final_index
    
    def add_opentype_features(self):
        """Add OpenType features for automatic composition"""
        self.font.addLookup("composites", "gsub_single", (), (
            ("ccmp", (("DFLT", ("dflt")),)),
        ))
        
        # Add compositional rules
        for initial in self.old_korean["initial_consonants"]:
            for vowel in self.old_korean["vowels"]:
                self.add_composition_rule(initial, vowel)
    
    def add_composition_rule(self, initial: str, vowel: str):
        """Add composition rule for automatic syllable formation"""
        lookup = self.font.getLookup("composites")
        subtable = lookup.addSubtable("composites_1")
        
        # Create substitution rule
        subtable.addPosSub(f"{initial}{vowel}", self.get_syllable_code_point(initial, vowel))
    
    def generate_all_combinations(self):
        """Generate all possible syllable combinations"""
        count = 0
        for initial in self.old_korean["initial_consonants"]:
            for vowel in self.old_korean["vowels"]:
                # Create basic syllable without final consonant
                self.create_syllable_block(initial, vowel)
                count += 1
                
                # Create syllables with final consonants
                for final in self.old_korean["final_consonants"]:
                    self.create_syllable_block(initial, vowel, final)
                    count += 1
        
        print(f"Generated {count} syllable combinations")
    
    def add_metadata(self):
        """Add font metadata"""
        self.font.copyright = "Created with OldKoreanFontForge"
        self.font.version = "1.0"
        self.font.weight = "Regular"
        
    def generate_font(self, output_path: str):
        """Generate the final font file"""
        self.font.generate(output_path)
        print(f"Font generated: {output_path}")

def main():
    # Create font forge instance
    forge = OldKoreanFontForge("CompleteOldKorean")
    
    # Create base glyphs
    forge.create_base_glyphs()
    
    # Generate all possible combinations
    forge.generate_all_combinations()
    
    # Add OpenType features
    forge.add_opentype_features()
    
    # Add metadata
    forge.add_metadata()
    
    # Generate font file
    forge.generate_font("CompleteOldKorean.ttf")

if __name__ == "__main__":
    main()
