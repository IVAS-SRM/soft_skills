import easyocr

def text_render(file_path, text_file_name='result.txt'):
    render = easyocr.Reader(["ru", "en"])
    result = render.readtext(file_path, detail=0, paragraph=True )
    
    with open(text_file_name, 'w') as file:
        for line in result:
            file.write(f'{line}\n\n')
    return f'Result {text_file_name}'

def main():
    file_patn = input('Enter a file patn: ')
    print('Process...')
    print(text_render(file_path=file_patn, text_file_name='read_me.txt'))

if __name__ == "__main__":
    main()
