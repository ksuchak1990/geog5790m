<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method='xml' doctype-system='http://www.w3.org/TR/2000/03/WD-SVG-20000303/DTD/svg-20000303-stylable.dtd' doctype-public='-//W3C//DTD SVG 20000303 Stylable//EN' />

<xsl:template match="/">


<svg width="100%" height="100%" version="1.1" xmlns="http://www.w3.org/2000/svg">

<xsl:for-each select="/map/polygon">
<polygon style="fill:#cccccc;stroke:#000000;stroke-width:1">
	<xsl:attribute name="points"><xsl:value-of select="points"/></xsl:attribute>
</polygon>
</xsl:for-each>
</svg>
</xsl:template>
</xsl:stylesheet>

