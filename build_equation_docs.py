from converter import PublicationConverter


if __name__ == "__main__":
    converter = PublicationConverter()
    result = converter.build_equation_documents_from_catalog(title="Publication scientifique")

    if result:
        print("Documents générés avec succès")
        print(f"Répertoire: {result['output_dir']}")
        print(f"Markdown: {result['markdown_doc']}")
        print(f"HTML: {result['html_doc']}")
    else:
        print("Échec de génération des documents")

