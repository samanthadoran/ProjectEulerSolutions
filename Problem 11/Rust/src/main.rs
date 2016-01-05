use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;
use std::cmp;

//Returns the largest product of four horizontally adjacent numbers starting at (x, y)
fn horizontal(grid: &Vec<Vec<u64>>, x: usize, y: usize) -> u64{
    let mut left: u64 = 1;
    let mut right: u64 = 1;

    for i in 0..4 {
        //Strange limiting check due to usize, make sure it didn't wraparound
        if i <= x {
            left *= grid[y][x - i];
        }
        if x + i < grid[y].len() {
            right *= grid[y][x + i];
        }
    }

    cmp::max(left, right)
}

//Returns the largest product of four vertically adjacent numbers starting at (x, y)
fn vertical(grid: &Vec<Vec<u64>>, x: usize, y: usize) -> u64{
    let mut up: u64 = 1;
    let mut down: u64 = 1;

    for i in 0..4 {
        //Strange limiting check due to usize, make sure it didn't wraparound
        if i <= y {
            up *= grid[y - i][x];
        }
        if y + i < grid.len() {
            down *= grid[y + i][x];
        }
    }

    cmp::max(up, down)
}

//Returns the largest product of four diagonally adjacent numbers starting at (x, y)
fn diagonal(grid: &Vec<Vec<u64>>, x: usize, y: usize) -> u64{
    let mut up_left: u64 = 1;
    let mut up_right: u64 = 1;
    let mut down_left: u64 = 1;
    let mut down_right: u64 = 1;

    for i in 0..4 {
        //Strange limiting check due to usize, make sure it didn't wraparound
        if i <= y {
            if i <= x {
                up_left *= grid[y - i][x - i];
            }
            if x + i < grid[y - i].len() {
                up_right *= grid[y - i][x + i];
            }
        }
        if y + i < grid.len() {
            //Strange limiting check due to usize, make sure it didn't wraparound
            if i <= x {
                down_left *= grid[y+i][x-i];
            }
            if x + i < grid[y + i].len() {
                down_right *= grid[y+i][x+i];
            }
        }
    }

    cmp::max(cmp::max(up_left, up_right), cmp::max(down_left, down_right))
}

//Read a grid of numbers into a 2d vector from a file
fn read_grid_from_file(filename: &str) -> Vec<Vec<u64>>{

    let mut grid: Vec<Vec<u64>> = Vec::new();
    //Let's assume the file exists and will open
    let f = (File::open(filename)).unwrap();
    //Get a reader to said file
    let reader = BufReader::new(f);

    //Iterate over the lines...
    for line in reader.lines() {
        //Rust is tedious about this
        let line = line.ok().expect("Is a string a string?");

        //Jump through hoops instead of using map to get the float equivalents
        let split = line.split(" ");
        let mut vec: Vec<u64> = vec![];
        for number in split {
            let x = match number.trim().parse() {
                Ok(num) => num,
                Err(_) => continue,
            };
            vec.push(x);
        }
        grid.push(vec)
    }
    return grid;
}

fn main() {
    let mut maximum = 0;

    //Read in grid...
    let grid: Vec<Vec<u64>> = read_grid_from_file("grid.txt");

    if grid.len() == 0 {
        println!("No numbers in the grid!");
        return;
    }

    for y in 0..grid.len() {
        for x in 0..grid[y].len() {
            maximum = cmp::max(horizontal(&grid, x, y), maximum);
            maximum = cmp::max(vertical(&grid, x, y), maximum);
            maximum = cmp::max(diagonal(&grid, x, y), maximum);
        }
    }
    println!("Largest product is: {}", maximum);
}
