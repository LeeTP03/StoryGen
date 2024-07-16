from openai import OpenAI
import os
import requests

API_KEY = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)

def make_story(story_prompt):
  story_generated = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are a best seller author that writes books for age 1-2"},
      {"role": "user", "content": story_prompt}
  ],
  temperature=1
  )
  return story_generated.choices[0].message.content

def make_cover_image_prompt(cover_prompt):
  cover_image_prompt = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "Based on the story given, You will design a detailed image prompt for the cover image of this story. The image prompt should include the theme of the story with relevant color, Keep it within 100 characters"},
      {"role": "user", "content": cover_prompt}
  ],
  temperature=1
  )
  return cover_image_prompt.choices[0].message.content

def make_cover_image(cover_image_prompt):
  image_generated = client.images.generate(
  model='dall-e-2',
  prompt = f"{cover_image_prompt}",
  size="256x256",
  quality="standard",
  n=1
  )

  return image_generated.data[0].url

def story_with_cover(prompt):
  story_text = make_story(prompt)
  cover_prompt = make_cover_image_prompt(story_text)
  cover_page = make_cover_image(cover_prompt)

  return story_text, cover_page
