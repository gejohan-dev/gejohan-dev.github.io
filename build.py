import os

print("Reading main.html...")
main_content = ""
with open("html/main.html", "r") as main_html_file:
    main_content = main_html_file.read()

index_html = "introduction.html"

print("Building html files based on main.html...")
for file_name in os.listdir("html"):
    print(file_name)

    file_content = ""
    with open(os.path.join("html", file_name), "r") as html_file:
        file_content = html_file.read()

    build_content = main_content.replace("{CONTENT}", file_content)
    with open(file_name, "w") as build_file:
        build_file.write(build_content)
        if file_name == index_html:
            print("Using this as index.html...")
            with open("index.html", "w") as index_html_file:
                index_html_file.write(build_content)

print("Done")
