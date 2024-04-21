import markdown_blocks as mb
import os
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    # Read the markdown from the from_path and store it as a Markdowm:
    with open(from_path, 'r') as markdown_file:
        markdown = markdown_file.read()


    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    markdown_parent_node = mb.markdown_to_html_node(markdown)
    html = markdown_parent_node.to_html()
    title = mb.extract_title(markdown)
    
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as html_file:
        print(template_content, file=html_file)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
        if not os.path.exists(dest_dir_path):
            os.mkdir(dest_dir_path)
        
        for filename in os.listdir(dir_path_content):
             print(f"The filename = {filename}")
             from_path = os.path.join(dir_path_content, filename)
             dest_path = os.path.join(dest_dir_path, filename)
             if dest_path.endswith(".md"):
                 dest_path = dest_path.replace(".md", ".html")
             print(f"destPath = {dest_path}")
             if os.path.isfile(from_path):
                generate_page(from_path=from_path, template_path=template_path, dest_path=dest_path)
             else:
                 generate_pages_recursive(from_path, template_path, dest_path)
            
            
             
