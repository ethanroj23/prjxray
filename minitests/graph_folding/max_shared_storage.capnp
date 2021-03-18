@0xc33b8dbf33893c3c;

struct CompactArray {
    storage :union {
        u8  @0 : List(UInt8);
        u16 @1 : List(UInt16);
        u32 @2 : List(UInt32);
        i8  @3 : List(Int8);
        i16 @4 : List(Int16);
        i32 @5 : List(Int32);
    }
}

struct WireToNodeStorage {
    # Storage of wire -> node patterns
    nodePatternDx         @0 : CompactArray;
    nodePatternDy         @1 : CompactArray;
    nodePatternToNodeWire @2 : CompactArray;

    # Storage of subgraph to wire
    subgraphs             @3 : List(CompactArray);

    nodePatterns        @4 : List(CompactArray);


    # Tile patterns
    tilePatterns          @5 : List(CompactArray);

    tilePkeys             @6 : CompactArray;
    tileToTilePatterns    @7 : CompactArray;
}

struct NodeToWiresStorage {
    # Storage of node -> wire patterns
    wirePatternDx       @0 : CompactArray; # all of the dxs (index lines up with index of nodeWireInTilePkeys maybe)
    wirePatternDy       @1 : CompactArray; # all of the dys
    wirePatternToWire   @2 : CompactArray; # all of the wirePattern Ending Wire pkeys

    # up to this point, the data is represented in the smallest possible representation

    # Storage of node to wire pattern lists. (index lines up with subgraphs)
    wirePatterns        @3 : List(CompactArray);

    # Storage of subgraph to node Subgraph contains starting_node_pkey
    subgraphs           @4 : List(CompactArray);

    # Tile patterns
    tilePatterns        @5 : List(CompactArray);

    tilePkeys           @6 : CompactArray;
    tileToTilePatterns  @7 : CompactArray;
}
