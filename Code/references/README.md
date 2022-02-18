# References

These are your robot building blocks. These functions must be used for our `skeletons`.
If you are adding _flare_ be sure to do so once the robot family is constructed.
The sample functions are taken directly from the processing website - they are examples of both _syntax_ and _useage_.

- (so you probably don't need the describe(), and you probably don't want to keep the same positions)

## python-mode

## p5js mode

### Draw a triangle

1. With coordinates (30, 75), (58, 20), (86, 75):

```JavaScript
triangle(30, 75, 58, 20, 86, 75);
describe('white triangle with black outline in mid-right of canvas');
```

#### Triangle syntax

```JavaScript
triangle(x1, y1, x2, y2, x3, y3)
```

Parameters:

- x1 Number: x-coordinate of the first point
- y1 Number: y-coordinate of the first point
- x2 Number: x-coordinate of the second point
- y2 Number: y-coordinate of the second point
- x3 Number: x-coordinate of the third point
- y3 Number: y-coordinate of the third point

### Draw a rectangle

1. At location (30, 20) with a width and height of 55:

```JavaScript
rect(30, 20, 55, 55);
describe('white rect with black outline in mid-right of canvas');
```

2. With rounded corners, each having a radius of 20:

```JavaScript
rect(30, 20, 55, 55, 20);
describe('white rect with black outline and round edges in mid-right of canvas');
```

#### Rectangle syntax

```JavaScript
rect(x, y, w, [h], [tl], [tr], [br], [bl])
```

Parameters:

- x Number: x-coordinate of the rectangle
- y Number: y-coordinate of the rectangle
- w Number: width of the rectangle
- h Number: height of the rectangle. (Optional)
- tl Number: optional radius of top-left corner. (Optional)
- tr Number: optional radius of top-right corner. (Optional)
- br Number: optional radius of bottom-right corner. (Optional)
- bl Number:optional radius of bottom-left corner. (Optional)

### Draw an ellipse

1. At location (30, 30) with a diameter of 20:

```JavaScript
ellipse(30, 30, 20);
describe('white ellipse with black outline in middle of a gray canvas');
```

#### Ellipse syntax

```JavaScript
ellipse(x, y, w, [h])
```

Parameters:

- x Number: x-coordinate of the center of ellipse
- y Number: y-coordinate of the center of ellipse
- w Number: width of the ellipse
- h Number: height of the ellipse. (Optional)
