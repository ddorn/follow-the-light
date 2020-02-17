#version 330

in vec2 bulb_pos;
in vec3 f_color;
in vec2 f_tex_coord;

uniform sampler2D tex;

float LIMIT = 100.0;

float mandelbrot(vec2 pos) {
    vec2 z = vec2(0.0, 0.0);
    for (float i = 0.0; i <= 1.0; i += 1.0/LIMIT) {
        z = vec2(
            pos.x + z.x*z.x - z.y*z.y,
            pos.y + 2.0 * z.x * z.y
        );

        if (z.x*z.x + z.y*z.y > 4.0) {
            return i;
        }
    }

    return 1.0;
}

void main() {
    vec4 co = vec4(f_color, 1.0) * clamp(0.5 + mandelbrot(bulb_pos), 0.0, 1.0);
    gl_FragColor = texture(tex, f_tex_coord + co.xy - co.xy);
//    gl_FragColor = vec4(f_tex_coord, co.x, 1.);
}