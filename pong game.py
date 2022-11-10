from turtle import Turtle,Screen
from paddle import Paddle;
from ball import Ball
from paddle import Paddle;
from scoreboard import Scoreboard;
import time;
paddle=Turtle();
screen=Screen();
screen.bgcolor("black");
screen.setup(800,600)
screen.title("Pong");
screen.tracer(0);


ball=Ball();
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
scoreboard=Scoreboard();


# def go_up():
#     new_y=paddle.ycor()+20;
#     paddle.goto(paddle.xcor(),new_y);
# def go_down():
#     new_y=paddle.ycor()-20;
#     paddle.goto(paddle.xcor(),new_y);
screen.listen();
screen.onkey(r_paddle.go_up,"Up");
screen.onkey(r_paddle.go_down,"Down");
screen.onkey(l_paddle.go_up,"w");
screen.onkey(l_paddle.go_down,"s");

game_is_on=True;
while game_is_on:
    screen.update();
    ball.move();
    time.sleep(ball.move_speed);
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y();
    if ball.distance(r_paddle)<70 and ball.xcor()>320 or ball.distance(l_paddle)<70 and ball.xcor()<-320:
        ball.bounce_x();
    #detect when r_paddle misses
    if ball.xcor()>380:
        ball.reset_position();
        scoreboard.l_point();
    if ball.xcor()<-380:
        ball.reset_position();
        scoreboard.r_point();















screen.exitonclick()