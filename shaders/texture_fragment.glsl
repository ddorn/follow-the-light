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

    vec2 a = vec2(0.15);
    inner_pos = clamp(inner_pos / (2.0 * a), 0.0, 0.5)
        + clamp((inner_pos - 1.0) / (2.0 * a) + 0.5, 0.0, 0.5);
    return (ipos + inner_pos) / tex_size;
}


vec4 blur(vec2 pos, float z) {
    float factor = 3.0;

    vec4 color = vec4(0.0);
    float half_size = factor * z*z;
    for (float dx = -half_size; dx < half_size; ++dx) {
        for (float dy = -half_size; dy < half_size; ++dy) {
            color += texture(tex, vec2(pos + vec2(dx, dy) / tex_size));
        }
    }
    return color / pow(ceil(2.*half_size), 2.0);
}

void main() {

//    if (f_pos.z < -0.2) {
//        gl_FragColor = blur(f_tex_coord, f_pos.z);
//    } else {
        gl_FragColor = texture(tex, fix(f_tex_coord));
//    }
}