<?php

class UserService {

    public function getUser($id) {
        $conn = new PDO("mysql:host=localhost;dbname=test", "root", "");

        $query = "SELECT * FROM users WHERE id = " . $id;
        $result = $conn->query($query);

        $user = $result->fetch();

        if ($user != null) {
            if ($user["active"] == 1) {
                return $user;
            } else {
                echo "User is inactive";
            }
        } else {
            echo "User not found";
        }
    }

    public function saveUser($user) {
        $conn = new PDO("mysql:host=localhost;dbname=test", "root", "");

        $sql = "INSERT INTO users (name, email) VALUES ('" . $user["name"] . "', '" . $user["email"] . "')";
        $conn->exec($sql);

        echo "User saved";
    }

    public function deleteUser($id) {
        $conn = new PDO("mysql:host=localhost;dbname=test", "root", "");

        $conn->exec("DELETE FROM users WHERE id = " . $id);

        echo "User deleted";
    }
}

?>