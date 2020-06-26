import java.util.Random;

public class matrix_mul{
  static int N = 1000;
  static Random ran = new Random();
  public static void main(String args[]){
    int [][]a = new int[N][N];
    int [][]b = new int[N][N];
    initialization(a,b);
    kij(a,b);
    ikj(a,b);
    jik(a,b);
    ijk(a,b);
    kji(a,b);
    jki(a,b);
  }
  public static void initialization(int[][]a, int[][]b){
    for(int i=0; i<N; i++){
      for(int j=0; j<N; j++){
        a[i][j] = ran.nextInt(100);
        b[i][j] = ran.nextInt(100);
      }
    }
  }
  public static void ijk(int[][]a, int[][]b){
    int[][] c = new int[N][N];
    long startTime=System.currentTimeMillis();
    for(int i=0; i<N; i++){
      for(int j=0; j<N; j++){
        for(int k=0; k<N; k++){
          c[i][j] = a[i][k] + b[k][j];
        }
      }
    }
    long endTime=System.currentTimeMillis();
    System.out.println("Execution time for i-j-k: "+(endTime-startTime)+"ms");
  }
  public static void ikj(int[][]a, int[][]b){
    int[][] c = new int[N][N];
    long startTime=System.currentTimeMillis();
    for(int i=0; i<N; i++){
      for(int k=0; k<N; k++){
        for(int j=0; j<N; j++){
          c[i][j] = a[i][k] + b[k][j];
        }
      }
    }
    long endTime=System.currentTimeMillis();
    System.out.println("Execution time for i-k-j: "+(endTime-startTime)+"ms");
  }
  public static void jik(int[][]a, int[][]b){
    int[][] c = new int[N][N];
    long startTime=System.currentTimeMillis();
    for(int j=0; j<N; j++){
      for(int i=0; i<N; i++){
        for(int k=0; k<N; k++){
          c[i][j] = a[i][k] + b[k][j];
        }
      }
    }
    long endTime=System.currentTimeMillis();
    System.out.println("Execution time for j-i-k: "+(endTime-startTime)+"ms");
  }
  public static void jki(int[][]a, int[][]b){
    int[][] c = new int[N][N];
    long startTime=System.currentTimeMillis();
    for(int j=0; j<N; j++){
      for(int k=0; k<N; k++){
        for(int i=0; i<N; i++){
          c[i][j] = a[i][k] + b[k][j];
        }
      }
    }
    long endTime=System.currentTimeMillis();
    System.out.println("Execution time for j-k-i: "+(endTime-startTime)+"ms");
  }
  public static void kij(int[][]a, int[][]b){
    int[][] c = new int[N][N];
    long startTime=System.currentTimeMillis();
    for(int k=0; k<N; k++){
      for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
          c[i][j] = a[i][k] + b[k][j];
        }
      }
    }
    long endTime=System.currentTimeMillis();
    System.out.println("Execution time for k-i-j: "+(endTime-startTime)+"ms");
  }
  public static void kji(int[][]a, int[][]b){
    int[][] c = new int[N][N];
    long startTime=System.currentTimeMillis();
    for(int k=0; k<N; k++){
      for(int j=0; j<N; j++){
        for(int i=0; i<N; i++){
          c[i][j] = a[i][k] + b[k][j];
        }
      }
    }
    long endTime=System.currentTimeMillis();
    System.out.println("Execution time for k-j-i: "+(endTime-startTime)+"ms");
  }
}