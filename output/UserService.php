<?php

class Database {
    private static ?Database $instance = null;
    private PDO $conn;

    private function __construct() {
        $this->conn = new PDO("mysql:host=" . getenv('DB_HOST') . ";dbname=" . getenv('DB_NAME'), getenv('DB_USER'), getenv('DB_PASS'));
        $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }

    public static function getInstance(): PDO {
        if (self::$instance === null) {
            self::$instance = new Database();
        }
        return self::$instance->conn;
    }
}

class UserService {
    private PDO $conn;

    public function __construct(PDO $pdo) {
        $this->conn = $pdo;
    }

    /**
     * Retrieve a user by ID.
     *
     * @param int $id User ID
     * @return array User data
     * @throws Exception If user is not found or inactive
     */
    public function getUser(int $id): array {
        try {
            $stmt = $this->conn->prepare("SELECT * FROM users WHERE id = :id");
            $stmt->execute(['id' => $id]);
            $user = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($user) {
                if ($user["active"] == 1) {
                    return $user;
                } else {
                    throw new Exception("User is inactive");
                }
            } else {
                throw new Exception("User not found");
            }
        } catch (PDOException $e) {
            // Log error
            throw new Exception("Database error: " . $e->getMessage());
        }
    }

    /**
     * Save a new user.
     *
     * @param array $user User data
     * @return string Confirmation message
     * @throws Exception If user data is invalid
     */
    public function saveUser(array $user): string {
        // Validate user input here
        if (empty($user["name"]) || empty($user["email"])) {
            throw new Exception("Invalid user data");
        }

        try {
            $stmt = $this->conn->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
            $stmt->execute(['name' => $user["name"], 'email' => $user["email"]]);
            return "User saved";
        } catch (PDOException $e) {
            // Log error
            throw new Exception("Database error: " . $e->getMessage());
        }
    }

    /**
     * Delete a user by ID.
     *
     * @param int $id User ID
     * @return string Confirmation message
     */
    public function deleteUser(int $id): string {
        try {
            $stmt = $this->conn->prepare("DELETE FROM users WHERE id = :id");
            $stmt->execute(['id' => $id]);
            return "User deleted";
        } catch (PDOException $e) {
            // Log error
            throw new Exception("Database error: " . $e->getMessage());
        }
    }
}

// Usage
try {
    $pdo = Database::getInstance();
    $userService = new UserService($pdo);
    // Call methods on $userService
} catch (Exception $e) {
    // Handle connection errors
    echo "Error: " . $e->getMessage();
}
?>