def interpolateown(upperR,lowerR,midR,upper,lower):
    return lower+(upper-lower)*(midR-lowerR)/(upperR-lowerR)