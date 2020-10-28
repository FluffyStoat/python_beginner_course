import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class TaskList {
    private static void check(List<Integer> values) {
        values.sort(Integer::compareTo);

        var ranges = new ArrayList<String>();
        var start = values.get(0);
        var len = values.size();

        for (int i = 0; i < len; i++) {
            var cur = values.get(i);
            if (i < len - 1) {
                var next = values.get(i + 1);
                if (cur + 1 != next) {
                    addRange(ranges, start, cur);
                    start = next;
                }
            }

            if (i == len - 1) {
                addRange(ranges, start, cur);
            }
        }

        System.out.println(String.format("%s => %s", values, ranges));
    }

    private static void addRange(List<String> ranges, Integer start, Integer end) {
        if (!start.equals(end)) {
            ranges.add(String.format("%d-%d", start, end));
        } else {
            ranges.add(String.format("%d", end));
        }
    }

    public static void main(String[] args) {
        var array1 = new Integer[] {1, 4, 5, 2, 3, 9, 8, 11, 0};
        var array2 = new Integer[] {1, 4, 3, 2};
        var array3 = new Integer[] {1, 4};

        check(Arrays.asList(array1));
        check(Arrays.asList(array2));
        check(Arrays.asList(array3));
    }
}