import os
import sqlite3
from typing import Dict, Optional, Any


class UserRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def find_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Find a user by their ID.

        Args:
            user_id (int): The ID of the user to find.

        Returns:
            Optional[Dict[str, Any]]: The user data if found, otherwise None.
        """
        try:
            stmt = self.conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            return stmt.fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def save_user(self, user: Dict[str, Any]) -> None:
        """Save a new user to the database.

        Args:
            user (Dict[str, Any]): The user data to save.
        """
        try:
            self.conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user["name"], user["email"]))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def delete_user(self, user_id: int) -> None:
        """Delete a user from the database.

        Args:
            user_id (int): The ID of the user to delete.
        """
        try:
            self.conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> Dict[str, Any]:
        """Retrieve a user by their ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Dict[str, Any]: The user data.

        Raises:
            Exception: If the user is inactive or not found.
        """
        user = self.user_repository.find_user_by_id(user_id)
        if user:
            if user.get("active") == 1:
                return user
            else:
                raise Exception("User is inactive")
        else:
            raise Exception("User not found")

    def save_user(self, user: Dict[str, Any]) -> None:
        """Save a new user.

        Args:
            user (Dict[str, Any]): The user data to save.
        """
        self.user_repository.save_user(user)

    def delete_user(self, user_id: int) -> None:
        """Delete a user.

        Args:
            user_id (int): The ID of the user to delete.
        """
        self.user_repository.delete_user(user_id)


def main() -> None:
    """Main function to set up the database connection and user service."""
    try:
        conn = sqlite3.connect(os.getenv('DB_NAME', 'users.db'))  # Use a default for demonstration
        user_repo = UserRepository(conn)
        user_service = UserService(user_repo)
        # Now you can use user_service to manage users
    except Exception as e:
        print(f"Database connection failed: {e}")


if __name__ == "__main__":
    main()