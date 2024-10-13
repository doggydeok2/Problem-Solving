import java.io.*;
import java.util.*;

public class Main {
    private void solution() throws Exception {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var st = new StringTokenizer(br.readLine());
        var n = Integer.parseInt(st.nextToken());
        var m = Integer.parseInt(st.nextToken());
        var cmd = new int[3];
        var balls = new int[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++)
                cmd[j] = Integer.parseInt(st.nextToken());

            int start = cmd[0], end = cmd[1], ball = cmd[2];
            for (int j = start; j < end + 1; j++)
                balls[j] = ball;
        }

        var sb = new StringBuilder();
        for (int i = 1; i < n + 1; i++)
            sb.append(balls[i]).append(' ');
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}