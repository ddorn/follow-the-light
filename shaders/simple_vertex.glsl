#version 330

in vec2 vert;
in vec2 tex_coord;
out vec3 f_color;
out vec2 bulb_pos;
out vec2 f_tex_coord;

uniform vec4 rects[10];
uniform uint sprite_id;
uniform float time;

float random(vec2 pos, float t) {
    return fract(sin(dot(pos, vec2(1232.12, 2342.234))) * 21313.4231 + t);
}

// All components are in the range [0…1], including hue.
// From https://stackoverflow.com/a/17897228
vec3 hsv2rgb(vec3 c)
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

void main() {
    bulb_pos = vec2(vert.x*1.5 - 0.5, vert.y * 1.5);

//    f_color = (vec3(random(vert)));
    f_color = hsv2rgb(vec3(random(vert, time / 5.), 1.0, 1.0));

    f_tex_coord = rects[sprite_id].xy + rects[sprite_id].zw * tex_coord;
    gl_Position = vec4(vert, 0.0, 1.0);
}
