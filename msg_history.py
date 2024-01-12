import streamlit as st
from pymongo import MongoClient


# Connect with Mongo DB
def db_connection():
    return MongoClient(st.secrets['db_connect'])


client = db_connection()


@st.cache_data(ttl=300)
def get_message_history():
    db = client.HBO_prod
    records = db.messages.find()
    records = list(records)
    return records


def create_message(msg):
    db = client.HBO_prod
    records = db.messages
    new_record = records.insert_one(msg)
    return new_record
