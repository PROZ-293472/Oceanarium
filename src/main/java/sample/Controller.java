package sample;

import java.io.FileReader;
import java.net.URL;
import java.sql.Connection;
import java.util.Iterator;
import java.util.ResourceBundle;


import db.DBConnection;
import javafx.fxml.Initializable;
import jdk.nashorn.internal.parser.JSONParser;
import org.json.JSONArray;
import org.json.JSONObject;


public class Controller implements Initializable{

    private Connection conn;

    public void initialize(URL url, ResourceBundle rb) {

        try {
            FileReader fr = new FileReader("C:\\Users\\Lenovo\\Desktop\\Studia\\WBD\\Oceanarium\\resources\\credentials.txt");
            String crd_txt = "";
            int c;
            while ((c=fr.read()) != -1)
                crd_txt += (char) c;

            System.out.println(crd_txt);

        } catch (Exception e) {
            e.printStackTrace();
        }



        conn = DBConnection.getConnection("A","B","C");
    }

}
