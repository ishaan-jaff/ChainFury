from database import db_session, ChatBot, Prompt
from sqlalchemy.orm import Session


def get_chatbots_from_username(db: Session, username: str):
    chatbots = []
    chatbots = db.query(ChatBot).filter(ChatBot.created_by == username).all()
    return chatbots


def get_prompts_from_chatbot_id(db: Session, chatbot_id: str):
    prompts = []
    prompts = db.query(Prompt).filter(Prompt.chatbot_id == chatbot_id).all()
    return prompts


def get_prompts_with_user_rating_from_chatbot_id(db: Session, chatbot_id: str):
    prompts = []
    prompts = db.query(Prompt).filter(Prompt.chatbot_id == chatbot_id, Prompt.user_rating != None).all()
    return prompts


def get_prompts_with_chatbot_user_rating_from_chatbot_id(db: Session, chatbot_id: str):
    prompts = []
    prompts = db.query(Prompt).filter(Prompt.chatbot_id == chatbot_id, Prompt.chatbot_user_rating != None).all()
    return prompts


def get_prompts_with_openai_rating_from_chatbot_id(db: Session, chatbot_id: str):
    prompts = []
    prompts = db.query(Prompt).filter(Prompt.chatbot_id == chatbot_id, Prompt.gpt_rating != None).all()
    return prompts
