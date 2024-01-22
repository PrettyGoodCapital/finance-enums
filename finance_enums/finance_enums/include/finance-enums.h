enum Foo {
  A = 1,
  B,
  C,
};
typedef uint32_t Foo;

typedef struct Point {
  float x;
  float y;
} Point;

char *version(void);

struct Point get_origin(void);

struct Point add_points(struct Point p1, struct Point p2);

bool is_in_range(struct Point point, float range);

void print_foo(const Foo *foo);
