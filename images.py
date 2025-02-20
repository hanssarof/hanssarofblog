import os
import re
import shutil

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"F:\1_DEV\0_PROJECTS\blog\hanssarofblog\content\posts"
attachments_dir = r"F:\_MYBRAIN\5. Les Images"
static_images_dir = r"F:\1_DEV\0_PROJECTS\blog\hanssarofblog\static\images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Step 2: Find all image links in the format ![[image.png#center]] or ![[image.png]]
        images = re.findall(r'!\[\[([^]#]*)(?:#center)?\]\]', content)
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatible link with Hugo-friendly centering
            markdown_image = f'<p style="text-align:center;"><img src="/images/{image.replace(" ", "%20")}" alt="Image Description"></p>'
            content = content.replace(f"![[{image}#center]]", markdown_image)
            content = content.replace(f"![[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")
