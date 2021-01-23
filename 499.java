public class Solution {
    public String findShortestWay(int[][] maze, int[] ball, int[] hole) {
        Queue<Point> queue = new LinkedList<>();
        int row = maze.length;
        int col = maze[0].length;
        Point[][] points = new Point[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                Point point = new Point(i, j);
                points[i][j] = point;
                if (i == hole[0] && j == hole[1]) {
                    point.path = "impossible";
                }
            }
        }
        int[] dirX = {0, -1, 1, 0}; // d, l, r, u
        int[] dirY = {1, 0, 0, -1};
        String[] dir = {"d", "l", "r", "u"};
        Point startPoint = points[ball[0]][ball[1]];
        startPoint.dis = 0;
        queue.add(startPoint);
        while (!queue.isEmpty()) {
            Point point = queue.poll();
            for (int i = 0; i < 4; i++) {
                int x = point.x;
                int y = point.y;
                int dis = point.dis;
                String path = point.path;
                boolean inHole = false;
                while (x >= 0 && x < row && y >= 0 && y < col && maze[x][y] == 0) {
                    x += dirX[i];
                    y += dirY[i];
                    dis++;
                    if (x == hole[0] && y == hole[1]) {
                        inHole = true;
                        break;
                    }
                }
                if (!inHole) {
                    x -= dirX[i];
                    y -= dirY[i];
                    dis--;
                }
                Point newPoint = points[x][y];
                if (newPoint.dis > dis) {
                    newPoint.dis = dis;
                    newPoint.path = String.join("", point.path, dir[i]);
                    if (!inHole) {
                        queue.add(newPoint);
                    }
                } else if (newPoint.dis == dis) {
                    boolean updated = false;
                    String newPath = String.join("", point.path, dir[i]);
                    for (int k = 0; k < newPoint.path.length() && k < newPath.length(); k++) {
                        if (newPoint.path.charAt(k) > newPath.charAt(k)) {
                            updated = true;
                            newPoint.path = newPath;
                            break;
                        }
                    }
                    if (!updated && newPoint.path.length() > newPath.length()) {
                        newPoint.path = newPath;
                    }
                }
            }
        }
        return points[hole[0]][hole[1]].path;
    }
}
class Point {
    int x;
    int y;
    String path;
    int dis;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
        this.path = "";
        this.dis = Integer.MAX_VALUE;
    }
}　　