package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	OUTPUT_FILENAME = "output.txt"
)

func main() {
	args := os.Args
	if len(args) != 2 {
		os.Exit(0)
	}

	inputFilename := args[1]
	inputFile, err := os.Open(inputFilename)
	if err != nil {
		fmt.Println("Could not open input file")
		os.Exit(1)
	}
	defer inputFile.Close()

	zeros := 0
	current := 50

	scanner := bufio.NewScanner(inputFile)
	for scanner.Scan() {
		line := scanner.Text()
		line = strings.TrimSpace(line)
		if line == "" {
			fmt.Println("Finished parsing")
			break
		}

		dir := string(line[0])
		rot, err := strconv.Atoi(line[1:])
		if err != nil {
			fmt.Println("Failed to parse int")
			break
		}

		if dir == "L" {
			current = (100 + current - rot) % 100
		} else {
			current = (current + rot) % 100
		}

		if current == 0 {
			zeros += 1
		}

		// fmt.Printf("Dir: %s, Rot: %d\n", dir, rot)
	}

	// TODO: Why is this here?
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file: ", err)
	} else {
		fmt.Printf("Total Zeros: %d\n", zeros)
	}
}
