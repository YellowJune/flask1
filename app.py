
m flask import Flask, request, send_file
import turtle
import io
from PIL import Image

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_turtle():
        code = request.json.get('code', '')

            # Turtle 그래픽 실행
                screen = turtle.Screen()
                    screen.setup(width=500, height=500)
                        t = turtle.Turtle()

                            try:
                                        exec(code, {'t': t, 'turtle': turtle})
                                                canvas = screen.getcanvas()
                                                        canvas.postscript(file="output.ps")

                                                                img = Image.open("output.ps")
                                                                        img.save("output.png")

                                                                                return send_file("output.png", mimetype='image/png')
                                                                                except Exception as e:
                                                                                            return {"error": str(e)}, 400
                                                                                            finally:
                                                                                                        turtle.bye()

                                                                                                        if __name__ == "__main__":
                                                                                                                app.run(host='0.0.0.0', port=5000)


                                                                                                    
