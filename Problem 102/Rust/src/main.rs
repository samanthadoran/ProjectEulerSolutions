use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;

struct Point {
    x: f64,
    y: f64,
}
//Determines the area of a triangle via it's vertices in coordinate space given by
//area = |Ax(By - Cy) + Bx(Cy - Ay) + Cx(Ay - By)|/2
fn area_of_triangle(a: &Point, b: &Point, c: &Point) -> f64 {
    (a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y)).abs()/2.0
}

//Test for floating point equality
fn feq(a: f64, b: f64) -> bool {
    (a - b).abs() < 0.00001
}

fn main() {
    let mut success_count = 0;

    //The point we are testing against, the origin
    let o = Point {x: 0.0, y: 0.0};

    //Let's assume the file exists and will open
    let f = (File::open("foo.txt")).unwrap();
    //Get a reader to said file
    let reader = BufReader::new(f);

    //Iterate over the lines...
    for line in reader.lines() {
        //Rust is tedious about this
        let line = line.ok().expect("Is a string a string?");

        //Jump through hoops instead of using map to get the float equivalents
        let split = line.split(",");
        let mut vec: Vec<f64> = vec![];
        for number in split {
            let x = match number.trim().parse() {
                Ok(num) => num,
                Err(_) => continue,
            };
            vec.push(x);
        }

        //Awful magic numbers are awful, but they work.
        let a = Point{x: vec[0], y: vec[1]};
        let b = Point{x: vec[2], y: vec[3]};
        let c = Point{x: vec[4], y: vec[5]};

        //This proof works by stating that the origin intersects if the areas made by replacing each
        //vertex to form three different triangles sum up to the original area of the triangle!
        let area = area_of_triangle(&a, &b, &c);

        let sum_sub_triangles = area_of_triangle(&a, &b, &o)
                                + area_of_triangle(&b, &c, &o)
                                + area_of_triangle(&c, &a, &o);

        //If the origin is in, increase the count!
        if feq(sum_sub_triangles, area) {
            success_count += 1;
        }
    }
    println!("Count: {}", success_count);
}
