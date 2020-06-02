package db;

import java.sql.*;
import javafx.scene.control.Alert;

public class DBConnection {

    private static Connection conn;

    public static Connection getConnection(String url, String username, String password) {
        try {
            conn = DriverManager.getConnection(url, username, password);
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setContentText("Ur connected bitch");
            alert.show();
        } catch (SQLException exc) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error to database connection");
            alert.setContentText("Details: "+ exc.getMessage());
            alert.show();
        }
        return conn;
    }
}
