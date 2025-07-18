#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File name: score_dao.py

Description:
    This module provides data access functions for managing scores in a SQLite
    database.

Functions:
    - create_scores_table: Creates the scores table if it does not exist.
    - insert_score: Inserts a new score into the scores table.
    - get_scores: Retrieves scores for a specific user and module.
    - update_score: Updates the score for a specific user and module.
    - delete_score: Deletes the score for a specific user and module.
    - initialize_database: Initializes the database and creates the scores
    table.

Author:
    Wesley Xavier <wesley.xvier@gmail.com>

Created on:
    2025-07-16

Version:
    1.0.0

License:
    MIT License
    Copyright (c) 2025 ProStudents Ltda.
"""
import sqlite3
from connection_factory.database_connection import (
    get_db_connection as get_connection
)

TABLE_NAME = 'scores'


def create_scores_table():
    """Create the scores table if it does not exist."""
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    module_id INTEGER NOT NULL,
                    score INTEGER DEFAULT 0,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while creating the table: {e}")
        finally:
            conn.close()
    else:
        print("Failed to create a database connection.")


def insert_score(user_id, module_id, score):
    """Insert a new score into the scores table."""
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f'''
                INSERT INTO {TABLE_NAME} (user_id, module_id, score)
                VALUES (?, ?, ?)
            ''', (user_id, module_id, score))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while inserting the score: {e}")
        finally:
            conn.close()
    else:
        print("Failed to create a database connection.")


def get_scores(user_id, module_id):
    """Retrieve scores for a specific user and module."""
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f'''
                SELECT * FROM {TABLE_NAME}
                WHERE user_id = ? AND module_id = ?
            ''', (user_id, module_id))
            scores = cursor.fetchall()
            return scores
        except sqlite3.Error as e:
            print(f"An error occurred while retrieving scores: {e}")
            return []
        finally:
            conn.close()
    else:
        print("Failed to create a database connection.")
        return []


def update_score(user_id, module_id, score):
    """Update the score for a specific user and module."""
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f'''
                UPDATE {TABLE_NAME}
                SET score = ?
                WHERE user_id = ? AND module_id = ?
            ''', (score, user_id, module_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while updating the score: {e}")
        finally:
            conn.close()
    else:
        print("Failed to create a database connection.")


def delete_score(user_id, module_id):
    """Delete the score for a specific user and module."""
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f'''
                DELETE FROM {TABLE_NAME}
                WHERE user_id = ? AND module_id = ?
            ''', (user_id, module_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while deleting the score: {e}")
        finally:
            conn.close()
    else:
        print("Failed to create a database connection.")


def initialize_database():
    """Initialize the database and create the scores table."""
    create_scores_table()


# Example usage of the DAO functions
if __name__ == "__main__":
    initialize_database()
    try:
        conn = get_connection()
        if conn:
            print("Database initialized and connection established.")
            insert_score(1, 101, 85)
            insert_score(1, 102, 90)
            scores = get_scores(1, 101)
            print(f"Scores for user 1, module 101: {scores}")
        else:
            print("Failed to connect to the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
