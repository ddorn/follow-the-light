#version 330

in vec2 f_tex_coord;
in vec3 f_pos;

uniform sampler2D tex;
uniform vec2 tex_size;
uniform vec2 screen_size;


/// Performs pixelart scale by fixing coordinates
vec2 fix(vec2 coord) {
    vec2 scaled = f_tex_coord * tex_size;

    vec2 ipos = floor(scaled);
    vec2 inner_pos = fract(scaled);

    vec2 a = vec2(0.4);
    inner_pos = clamp(inner_pos / (2.0 * a), 0.0, 0.5)
        + clamp((inner_pos - 1.0) / (2.0 * a) + 0.5, 0.0, 0.5);
    return (ipos + inner_pos) / tex_size;
}


void main() {
    gl_FragColor = texture(tex, fix(f_tex_coord));
}