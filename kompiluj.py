from saxonche import PySaxonProcessor

def compile_xslt_to_sef():
    with PySaxonProcessor(license=False) as proc:
        print("Iniciujem Saxon procesor...")
        xslt_proc = proc.new_xslt30_processor()
        
        print("Kompilujem 'stylesheet-ubl.xslt' do JSON formátu...")
        # Kompilácia šablóny priamo do výstupného súboru .sef.json
        xslt_proc.compile_stylesheet_to_file(
            stylesheet_file="stylesheet-ubl.xslt",
            output_file="stylesheet-ubl.sef.json"
        )
        
        print("Úspešne hotovo! Súbor 'stylesheet-ubl.sef.json' bol vygenerovaný.")

if __name__ == "__main__":
    compile_xslt_to_sef()