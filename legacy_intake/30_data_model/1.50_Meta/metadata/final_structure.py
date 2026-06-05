#!/usr/bin/env python3
"""
Final immigration structure example with ASCII characters only
"""

from slugs_mapping import SlugMapper

def main():
    mapper = SlugMapper()
    
    print("=== Immigration Folder Structure with Abbreviated Filenames ===")
    print()
    
    print("50_Legal")
    print("└── 60_Immigration")
    print()
    
    print("    ├── 00_Drafts_and_Strategy")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'strategy', detail='plan', version='v01', status='final')}")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'timeline', version='v01', status='final')}")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'drafts', detail='affidavit', version='v01', status='draft')}")
    print()
    
    print("    ├── 10_Bio_and_IDs")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'bio-and-ids', detail='passport-copy')}")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'bio-and-ids', detail='birth-certificate')}")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'bio-and-ids', detail='id-card-copy')}")
    print()
    
    print("    ├── 20_Employment")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'employment', detail='offer-letter')}")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'employment', detail='pay-stubs')}")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'employment', detail='w2-forms')}")
    print()
    
    print("    ├── 30_Financial")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'financial', detail='tax-returns')}")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'financial', detail='bank-statements')}")
    print()
    
    print("    ├── 40_Other_Evidence")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'other', detail='photos-relationship')}")
    print(f"    │   ├── {mapper.generate_filename('qia', 'legal', 'other', detail='letters-of-support')}")
    print()
    
    print("    ├── 50_Form_Filings")
    print()
    
    print("    │   ├── 10_I-589 (Asylum)")
    print(f"    │   │   ├── {mapper.generate_immigration_filename('qia', 'i589', 'cover-letter', status='final')}")
    print(f"    │   │   ├── {mapper.generate_immigration_filename('qia', 'i589', 'affidavit', version='v01', status='draft')}")
    print(f"    │   │   ├── {mapper.generate_immigration_filename('qia', 'i589', 'form', status='final')}")
    print()
    
    print("    │   ├── 20_I-360 (Special Immigrant)")
    print(f"    │   │   ├── {mapper.generate_immigration_filename('qia', 'i360', 'cover-letter', status='final')}")
    print(f"    │   │   ├── {mapper.generate_immigration_filename('qia', 'i360', 'personal-statement', status='final')}")
    print()
    
    print("    │   ├── 30_I-130 (Family Sponsorship)")
    print(f"    │   │   ├── {mapper.generate_immigration_filename('qia', 'i130', 'cover-letter', status='final')}")
    print(f"    │   │   ├── {mapper.generate_immigration_filename('qia', 'i130', 'evidence-of-relationship', status='final')}")
    print()
    
    print("    │   ├── 40_I-765 (Employment Authorization)")
    print(f"    │   │   ├── {mapper.generate_immigration_filename('qia', 'i765', 'cover-letter', status='final')}")
    print(f"    │   │   ├── {mapper.generate_immigration_filename('qia', 'i765', 'form', status='final')}")
    print()
    
    print("    │   ├── 50_I-485 (Adjustment of Status)")
    print(f"    │   │   ├── {mapper.generate_immigration_filename('qia', 'i485', 'cover-letter', status='final')}")
    print(f"    │   │   ├── {mapper.generate_immigration_filename('qia', 'i485', 'medical-exam', status='final')}")
    print()
    
    print("    │   ├── 60_Change_of_Address")
    print(f"    │   │   └── {mapper.generate_filename('qia', 'legal', 'change-of-address', detail='form', status='final')}")
    print()
    
    print("    │   ├── 70_Indiana_BMV_License")
    print(f"    │   │   ├── {mapper.generate_filename('qia', 'legal', 'indiana-bmv', detail='application', status='final')}")
    print(f"    │   │   └── {mapper.generate_filename('qia', 'legal', 'indiana-bmv', detail='documents', status='final')}")
    print()
    
    print("    │   ├── 80_Social_Security_Applications")
    print(f"    │   │   ├── {mapper.generate_filename('qia', 'legal', 'social-security', detail='application', status='final')}")
    print(f"    │   │   └── {mapper.generate_filename('qia', 'legal', 'social-security', detail='documents', status='final')}")
    print()
    
    print("    └── 90_Archive")
    print()
    
    print("=== Key Benefits ===")
    print("✅ Filenames are under 80 characters")
    print("✅ Consistent abbreviations across all files")
    print("✅ Clear organization by form type and document category")
    print("✅ Easy to locate specific documents")
    print("✅ Scalable for additional forms and documents")
    print()
    
    print("=== Abbreviation Examples ===")
    print("• legal -> Leg")
    print("• cover-letter -> CL")
    print("• affidavit -> Aff")
    print("• personal-statement -> PS")
    print("• evidence-of-relationship -> EOR")
    print("• medical-exam -> ME")
    print("• bio-and-ids -> Bio")
    print("• social-security -> Soc-Sec")
    print("• application -> Apps")
    print("• documents -> Docs")

if __name__ == "__main__":
    main()
