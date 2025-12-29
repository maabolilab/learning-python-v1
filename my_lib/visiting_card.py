
def print_visting_card(name, profession, phone):
    print("The card generation start's please wait a while....")
    file_name = f"{name.replace(' ', '_')}_card.html"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8"> 
        <title>{name}'s Card</title>
        <style>
            body {{ font-family: sans-serif; display: flex; justify-content: center; padding: 50px; }}
            .card {{
                width: 260px;
                padding: 20px;
                background-color: #FFD700; 
                border: 3px solid black;
                border-radius: 15px;
                text-align: center;
                box-shadow: 10px 10px 0px black;
                transition: transform 0.2s;
            }}
            .card:hover {{ transform: scale(1.05); }}
            .avatar {{
                width: 80px; height: 80px;
                border-radius: 50%;
                border: 3px solid black;
                background-color: white;
            }}
            .contact {{
                margin-top: 15px; background-color: white;
                border: 2px solid black; padding: 8px;
                border-radius: 8px; font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <!-- Magic Avatar Generator based on Name -->
            <img class="avatar" src="https://api.dicebear.com/7.x/avataaars/svg?seed={name}" alt="Avatar">
            
            <h1>{name}</h1>
            <p style="font-size: 18px;">⭐ {profession}</p>
            
            <div class="contact">
                📞 {phone}
            </div>
        </div>
    </body>
    </html>
    """

    # 3. Write to File
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ Success! Card created: {file_name}")