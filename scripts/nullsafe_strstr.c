#include <stddef.h>
#include <string.h>
/* Workaround for Blender 5.2 background startup with no Metal device.
 * Metal backend passes a null device name to libc strstr. Preserve libc
 * behavior for valid strings, return NULL for the unavailable name.
 * Only loaded into our background renderer; does not alter installed app. */
static char *safe_strstr(const char *h, const char *n) {
  if (!h || !n) return NULL;
  if (!*n) return (char *)h;
  for (; *h; h++) {
    const char *a=h,*b=n;
    while (*a && *b && *a==*b) {a++; b++;}
    if (!*b) return (char *)h;
  }
  return NULL;
}
__attribute__((used)) static struct { const void *replacement; const void *replacee; }
interpose __attribute__((section("__DATA,__interpose"))) = {(const void *)safe_strstr,(const void *)strstr};
