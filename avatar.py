from flask import render_template
from openai import OpenAI

def handle_avatar(form_data):
    body_type = form_data.get('body_type')
    skin_tone = form_data.get('skin_tone')
    hair_style = form_data.get('hair_style')
    dress_type = form_data.get('dress_type')

    # 🧠 Prompt for DALL·E
    prompt = f"A full-body digital illustration of a woman with {body_type} body type, {skin_tone} skin tone, {hair_style} hair, wearing a {dress_type}"

    try:
        # 🗝 Use your OpenAI API key here
        client = OpenAI(api_key="your_api")

        # 🎨 Generate image
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )

        image_url = response.data[0].url

    except Exception as e:
        image_url = None
        print("❌ Error generating image:", e)

    return render_template('avatar_result.html',
                           body_type=body_type,
                           skin_tone=skin_tone,
                           hair_style=hair_style,
                           dress_type=dress_type,
                           image_url=image_url)