#version 330

in vec2 f_tex_coord;
uniform sampler2D tex;
uniform vec2 tex_size;
uniform vec2 screen_size;


/// Performs pixelart scale by fixing coordinates
vec2 fix(vec2 coord) {
    vec2 scaled = f_tex_coord * tex_size;

    vec2 ipos = floor(scaled);
    vec2 inner_pos = fract(scaled);

    vec2 a = vec2(0.15);
    inner_pos = clamp(inner_pos / (2.0 * a), 0.0, 0.5)
        + clamp((inner_pos - 1.0) / (2.0 * a) + 0.5, 0.0, 0.5);
    return (ipos + inner_pos) / tex_size;
}

void main() {

    vec4 color = texture(tex, fix(f_tex_coord));
//    color.a = color.a < 1.0 ? 0.0 : 1.0;
    gl_FragColor = color;
//    gl_FragColor = vec4(fix(f_tex_coord), 0.0, 1.0);
}