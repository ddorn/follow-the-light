#version 330

in vec2 vert;
in vec2 tex_coord;
in int sprite_id;

out vec3 f_color;
out vec2 f_tex_coord;

uniform vec4 rects[10];
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
    vec2 coord_inverted = rects[sprite_id].xy + rects[sprite_id].zw * tex_coord.xy;
    f_tex_coord = coord_inverted;
//    gl_Position = vec4(vert.x + 2*fract(time / 15.0 * float(12 - sprite_id)), vert.y, 0.0, 1.0);
//    gl_Position = vec4(vert.x + float(sprite_id) / 10.0, vert.y + float(sprite_id) / 13.0, 0.0, 1.0 + time - time);
    gl_Position = vec4(vert, 0.0, 1.0 + time - time);
}
