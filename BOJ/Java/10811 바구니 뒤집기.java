import java.io.*;
import java.util.*;

public class Main {
    private Integer[] nums;

    private void swap(Integer s, Integer e) {
        var temp = nums[s];
        nums[s] = nums[e];
        nums[e] = temp;
    }
    private void solution() throws Exception {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var st = new StringTokenizer(br.readLine());
        var n = Integer.parseInt(st.nextToken());
        var m = Integer.parseInt(st.nextToken());
        nums = new Integer[n + 1];

        for (var i = 1; i <= n; i++)
            nums[i] = i;

        for (var i = 0; i < m; i++) {
            var input = br.readLine().split(" ");
            var s = Integer.parseInt(input[0]);
            var e = Integer.parseInt(input[1]);
            for (var j = 0; j < (e - s + 1) >> 1; j++)
                swap(s + j, e - j);
        }

        var sb = new StringBuilder();
        for (var i = 1; i <= n; i++)
            sb.append(nums[i]).append(" ");
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}