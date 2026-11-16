class Solution {
    public String digitSum(String s, int k) {
        StringBuilder res = new StringBuilder(s);

        System.out.println(res);
        while (res.length() > k) {
            StringBuilder nextRound = new StringBuilder();
            for (int i = 0; i < res.length(); i += k) {
                int sum = 0;
                for (int j = i; j < res.length() && j < i + k; j++) {
                    sum += res.charAt(j) - '0';
                    //sum += Integer.parseInt(res.charAt(j).toString());
                }
                System.out.print(sum + " ");
                nextRound.append(sum);
            }
            res = nextRound;
            System.out.println(res);
        }
        return res.toString();
    }
}