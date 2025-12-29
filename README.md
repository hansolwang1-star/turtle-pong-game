# turtle-pong-game

## Overview
This is a classic Pong game created in Python using only the Turtle graphics library and the `time` module for delays.
Full code available at [github.com/hansolwang1-star/turtle-pong-game]





## Challenges I Faced

### Bugs That Remain Unresolved
- Implementing accurate collision detection between the ball and the paddles  
  - The ball would occasionally pass through the paddles when hitting their sides
- Both paddles cannot be controlled simultaneously

### Other Challenges
- Keeping the ball movement and overall gameplay smooth  
  - Resolved by using `sc.tracer(0)` for manual screen updates processed on a `While True`

## Controls
- PlayerOne (Left Paddle):**`W` (up), `S` (down)
- PlayerTwo (Right Paddle):**`Up Arrow` (up), `Down Arrow` (down)

## Features
- Smooth gameplay using `tracer(0)` for manual screen updates
- Paddle Boundary: Limits paddles from moving off the screen
- Dynamic Scoring: First player to reach 10 points wins
- Starting Screen: Press `SpaceKey` to start

## Learning Outcomes
- Problem solving and creative thinking skills
- Importance of clean, readable, and well-documented code (eg. Meaningful Variable Names)

## Next Step
- Gradually increasing the ball speed over time by using the `time` module
- Adding sound effects by importing the `playsound` module
Pong game made only using turtle
