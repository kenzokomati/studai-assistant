def read_prompts_file(file_name: str) -> str:
    file_path = f"app/prompts/{file_name}.md"
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()