
import java.util.*;
import java.io.*;

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Klick
 */
public class tictactoe {
    
    final static String PROBLEM_NAME = "tictactoe";
    final static String WORK_DIR = "D:\\CodeJam\\" + PROBLEM_NAME + "\\";

    static int [][] board = new int[4][4];

    static void preprocess() {
        
    }
    
    void solve(Scanner sc, PrintWriter pw) {
        String s = sc.nextLine();
        int success = 0;
        for (int i=0; i<4; i++){
            s = sc.nextLine();
            int j = 0;
            
        for (char c : s.toCharArray()){
            if (c == 'X') {
                board[i][j] = 0;
            } 
            else if (c == 'O' ){
                board[i][j] = 1;
            }
            else if (c == 'T' ){
                board[i][j] = 2;
            }                                            
            else {
                board[i][j] = 3;
            }
            j++;
            }            
        }
        
        
        
        //check for X or O winning
        for (int i=0; i<4; i++){
            
            
            if( (board[i][0]==0||board[i][0]==2)&&(board[i][1]==0||board[i][1]==2)&&(board[i][2]==0||board[i][2]==2)&&(board[i][3]==0||board[i][3]==2)  ){
            if(success == 0)pw.print("X won");
            success = 1;
            
            }
            if( (board[i][0]==1||board[i][0]==2)&&(board[i][1]==1||board[i][1]==2)&&(board[i][2]==1||board[i][2]==2)&&(board[i][3]==1||board[i][3]==2)  ){
            if(success == 0)pw.print("O won");
            success = 1;
            }
            
            if( (board[0][i]==0||board[0][i]==2)&&(board[1][i]==0||board[1][i]==2)&&(board[2][i]==0||board[2][i]==2)&&(board[3][i]==0||board[3][i]==2)  ){
            if(success == 0)pw.print("X won");
            success = 1;
            }
            if( (board[0][i]==1||board[0][i]==2)&&(board[1][i]==1||board[1][i]==2)&&(board[2][i]==1||board[2][i]==2)&&(board[3][i]==1||board[3][i]==2)  ){
            if(success == 0)pw.print("O won");
            success = 1;
            }
            
            }
        
        if( (board[0][0]==0||board[0][0]==2)&&(board[1][1]==0||board[1][1]==2)&&(board[2][2]==0||board[2][2]==2)&&(board[3][3]==0||board[3][3]==2)  ){
            if(success == 0)pw.print("X won");
            success = 1;
            }
        if( (board[0][0]==1||board[0][0]==2)&&(board[1][1]==1||board[1][1]==2)&&(board[2][2]==1||board[2][2]==2)&&(board[3][3]==1||board[3][3]==2)  ){
            if(success == 0)pw.print("O won");
            success = 1;
            }
        if( (board[3][0]==0||board[3][0]==2)&&(board[2][1]==0||board[2][1]==2)&&(board[1][2]==0||board[1][2]==2)&&(board[0][3]==0||board[0][3]==2)  ){
            if(success == 0)pw.print("X won");
            success = 1;
            }
        if( (board[3][0]==1||board[3][0]==2)&&(board[2][1]==1||board[2][1]==2)&&(board[1][2]==1||board[1][2]==2)&&(board[0][3]==1||board[0][3]==2)  ){
            if(success == 0)pw.print("O won");
            success = 1;
            }
        
        
        if(success == 0)
        {
            for (int i=0; i<4; i++){
                for (int j=0; j<4; j++){
                    if(board[i][j]==3 && (success == 0)){
                        pw.print("Game has not completed");
                        success = 1;}                                            
                }
            }
            
        }
        
        if(success == 0)
        {
            pw.print("Draw");
        }
        
                
        
        //else last case
        
        
        pw.println();        
    }
    
    public static void main(String[] args) throws Exception {
        preprocess();

        Scanner sc = new Scanner(new FileReader(WORK_DIR + "input.txt"));
        PrintWriter pw = new PrintWriter(new FileWriter(WORK_DIR + "output.txt"));
        int caseCnt = sc.nextInt();
        for (int caseNum=0; caseNum<caseCnt; caseNum++) {
            System.out.println("Processing test case " + (caseNum + 1));
            pw.print("Case #" + (caseNum+1) + ": ");
            new tictactoe().solve(sc, pw);
        }
        pw.flush();
        pw.close();
        sc.close();
    }
}


