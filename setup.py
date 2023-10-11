import argparse
from bs4 import BeautifulSoup

def modify_html(title, description, favicon_path, input_file, output_file):
    # 读取HTML文件
    with open(input_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
    
    # 修改<title>标签的内容
    soup.title.string = title
    
    # 修改<meta name="description">标签的内容
    meta_description = soup.find('meta', {'name': 'description'})
    if meta_description:
        meta_description['content'] = description
    else:
        # 如果<meta name="description">不存在，则创建一个
        new_meta = soup.new_tag('meta', content=description, name='description')
        soup.head.append(new_meta)
    
    # 修改<link rel="icon">标签的href属性
    favicon = soup.find('link', {'rel': 'icon'})
    if favicon:
        favicon['href'] = favicon_path
    else:
        # 如果<link rel="icon">不存在，则创建一个
        new_favicon = soup.new_tag('link', href=favicon_path, rel='icon')
        soup.head.append(new_favicon)
    
    # 将修改后的HTML写入到新文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))




def main(args):
    modify_html(
        args.title,
        args.description,
        args.favicon,
        args.input_file,
        args.output_file
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modify HTML metadata.")
    parser.add_argument("-t", "--title", type=str, required=True, help="New title")
    parser.add_argument("-d", "--description", type=str, required=True, help="New description")
    parser.add_argument("-f", "--favicon", type=str, default='favicon.png', help="Path to new favicon")
    parser.add_argument("-i", "--input_file", type=str, default="index.html", help="Path to input HTML file")
    parser.add_argument("-o", "--output_file", type=str, default="index.html", help="Path to output HTML file")
    
    args = parser.parse_args()
    main(args)
